#!/usr/bin/env python3
""" Server Proto Class, Server Factory Class"""

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.defer import Deferred, DeferredList
import struct
import threading
import logging
from angrybirds.lib.error import DeferredCallbackError, ServerConnectClientError, ReceiveTimeoutError
from angrybirds.config.sim_env_config import PluginExeControlTimeout
from angrybirds.lib.watchdog import Watchdog
logger = logging.getLogger(__name__)


class DataInterface(Protocol):

    def __init__(self, factory):
        logger.debug("Initializing %s" % self.__class__.__name__)
        self.factory = factory
        self.deferred = None
        self.id = None
        self.buffer = b''
        logger.debug("Initialized %s" % self.__class__.__name__)

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.factory.addClient(self)
        self.id = self.factory.numProtocols - 1  # first init temporary plane id
        logger.debug("Server new connect: %d" % (self.factory.numProtocols))

    def connectionLost(self, reason):
        logger.debug("Server lost connect: %d %s" % (self.factory.numProtocols, reason))
        self.factory.numProtocols = self.factory.numProtocols - 1
        self.factory.delClient(self)

    def dataReceived(self, data):
        # logger.debug("Server receive %s" % str(data))
        self.buffer += data
        if self.deferred is None:
            return  # wait for first init deferred is done
        buf_len = len(self.buffer)
        if buf_len >= 4:
            pack_length = int.from_bytes(self.buffer[:4], byteorder='little', signed=True)
        else:
            return  # wait receive
        if buf_len >= pack_length + 4:
            pack_data = self.buffer[4:pack_length + 4]
            self.buffer = self.buffer[pack_length + 4:]
        else:
            return  # wait receive

        msg_type, plane_id = struct.unpack('<iB', pack_data[:5])
        if msg_type != 0:
            logger.error("packet data msg_type err: %d" % (msg_type))
            return  # error packet
        logger.debug(
            "Server receive done ready callback event,plane id: %s",
            str(plane_id),
        )
        self.id = plane_id - 1
        self.deferred.callback([self.id, pack_data[5:]])
        self.deferred = None
        self.buffer = b''

    def dataSend(self, data: bytes, deferred: Deferred):
        # logger.debug("Service send data: %s" % str(data))
        self.deferred = deferred
        if len(self.buffer) > 0:
            self.dataReceived(b'')  # first init active call and if buffer have data
        if data == b'':
            return
        send_buf = b''
        send_buf = struct.pack('<iB', 1, self.id + 1) + data
        send_buf = struct.pack('<I', len(send_buf)) + send_buf
        self.transport.write(send_buf)


class DataInterfaceFactory(Factory):

    def __init__(self, client_cnt: int):
        logger.debug("Initializing %s" % self.__class__.__name__)
        self.numProtocols = 0
        self.clients = []
        self.client_cnt = client_cnt
        self.clients_data = [None] * self.client_cnt
        self.clients_lock = threading.Lock()
        self.watchdog = Watchdog(PluginExeControlTimeout, self._handle, name='DataInterface')
        self.istimeout = False
        logger.debug("Initialized %s" % self.__class__.__name__)

    def buildProtocol(self, addr):
        logger.debug("Server has Client Connected")
        return DataInterface(self)

    def addClient(self, client):
        logger.debug("Server append Client to list")
        self.clients.append(client)

    def delClient(self, client):
        logger.debug("Server delete Client from list")
        self.clients.remove(client)

    def _handle(self):
        self.istimeout = True
        self.watchdog.stop()

    def check_client(self):
        self.watchdog.reset()
        while len(self.clients) < self.client_cnt:
            if self.istimeout:
                break
            continue  # wait client connected
        self.watchdog.stop()
        if len(self.clients) < self.client_cnt:
            raise ServerConnectClientError(
                "Server: the number of clients is less than the number of subscriptions")

    def initData(self) -> list:
        logger.debug("Server initing data from Client " + str(len(self.clients)) + " of " +
                     str(self.client_cnt))
        self.check_client()
        data = self.sendAll(data=[b''] * self.client_cnt)
        logger.debug("Server inited data from Client")
        return data

    def sendAll(self, data: list, timeout=PluginExeControlTimeout, non_blocked=False) -> list:
        # logger.debug("Server sending data: %s", str(data))
        if len(self.clients) < self.client_cnt:
            raise ServerConnectClientError(
                "Server: the number of clients is less than the number of subscriptions")
        logger.debug("Server wait all Client connected done")
        if self.clients_lock.locked():  # reset lock
            self.clients_lock.release()
        self.clients_lock.acquire()  # set lock is locked
        deferredList = []  # init wait client deferred list
        for i in range(len(data)):
            deferredList.append(Deferred())
        dl = DeferredList(deferredList, consumeErrors=True)
        dl.addCallback(self.process_event)  # wait send all client return done
        for client in self.clients:
            if isinstance(client.id, int) and client.id < len(data):
                client.dataSend(data[client.id], deferredList[client.id])
            else:
                logger.error("Server has Client ID is Error: {} overflow data length {}".format(
                    client.id, len(data)))
                raise ServerConnectClientError(
                    "Server has Client ID is Error: {} overflow data length {}".format(
                        client.id, len(data)))
        if non_blocked:
            return
        if not self.clients_lock.acquire(timeout=timeout):  # wait trigger lock is unlocked
            logger.error("Server wait client return data, timeout: %s" % str(timeout))
            raise ReceiveTimeoutError("Server wait Client return data timeout %s" % timeout)
        # logger.debug("Server sended data: %s" % str(self.clients_data))
        return self.clients_data

    def process_event(self, result):
        # logger.debug("Server process event starting %s" % str(result))
        self.clients_data = [None] * self.client_cnt
        for success, value in result:
            if success:
                plane_id, data = value
                self.clients_data[plane_id] = data
            else:
                raise DeferredCallbackError("Server wait Client callback Failure: %s" %
                                            value.getErrorMessage())
        # all client recevice event done
        if self.clients_lock.locked():
            self.clients_lock.release()
        logger.debug("Server process event ended")


if __name__ == "__main__":
    from twisted.internet import reactor
    factory = DataInterfaceFactory()
    endpoint = TCP4ServerEndpoint(reactor=reactor, port=60000, interface='127.0.0.1')
    endpoint.listen(factory)
    reactor.run()
