#!/usr/bin/env python3
""" Client Proto Class, Client Factory Class"""

from twisted.internet.protocol import Protocol, ReconnectingClientFactory
from twisted.internet.defer import Deferred
import struct
import threading
import logging
from angrybirds.lib.error import ReceiveTimeoutError, ClientConnectError
logger = logging.getLogger(__name__)


class ControllerProtocol(Protocol):

    def __init__(self):
        logger.debug("Initializing %s", self.__class__.__name__)
        self.connected = False
        self.buffer = b''
        self.deferred = None
        logger.debug("Initialized %s", self.__class__.__name__)

    def connectionMade(self):
        self.connected = True
        logger.debug("Client new connect")

    def connectionLost(self, reason):
        self.connected = False
        logger.debug("Client lost connect")

    def dataReceived(self, data):
        # logger.debug("Client receive %s", str(data))
        self.buffer += data
        if self.deferred is None:
            return  # server sends data to me, but i'm not sends any data
        buf_len = len(self.buffer)
        if buf_len >= 4:
            pack_length = int.from_bytes(self.buffer[:4], byteorder='little', signed=True)
            logger.debug("Client ready receive data length %s" % str(pack_length))
        else:
            return  # wait receive
        if buf_len >= pack_length + 4:
            pack_data = self.buffer[4:pack_length + 4]
            self.buffer = self.buffer[pack_length + 4:]
        else:
            return  # wait receive
        logger.debug("Client receive done ready callback event %s" % str(pack_data))
        self.deferred.callback(pack_data)
        self.deferred = None
        self.buffer = b''

    def dataSend(self, data: bytes, deferred):
        self.deferred = deferred
        send_buf = struct.pack('<I', len(data)) + data
        self.transport.write(send_buf)
        # logger.debug("Client send data: %s" % str(send_buf))


class ControllerClientFactory(ReconnectingClientFactory):
    maxDelay = 1
    initialDelay = 8

    def __init__(self):
        logger.debug("Initializing %s" % self.__class__.__name__)
        self.protocol = None
        self.__retry = 1
        self.server_data = None
        self.server_lock = threading.Lock()
        logger.debug("Initialized %s" % self.__class__.__name__)

    def startedConnecting(self, connector):
        logger.debug("Client Start to Connect")

    def buildProtocol(self, addr):
        logger.debug("Client Connected")
        self.__retry = 1
        self.protocol = ControllerProtocol()
        return self.protocol

    def clientConnectionLost(self, connector, reason):
        logger.debug("Client Lost connection. Reason: %s" % reason)
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        logger.debug("Client Connection is failed, Reason: %s, %s", reason,
                     "Retry {}".format(self.__retry))
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)
        self.__retry += 1

    def send(self, data=b'', timeout=5, non_blocked=False):
        # logger.debug("Client sending data: %s" % str(data))
        if non_blocked:
            self.protocol.dataSend(data, None)
            return
        if self.server_lock.locked():  # reset lock
            self.server_lock.release()
        self.server_lock.acquire()  # set lock is locked
        if self.protocol and self.protocol.connected:
            deferred = Deferred()
            deferred.addCallback(self.process_event)
            self.protocol.dataSend(data, deferred)
        else:
            raise ClientConnectError("Client send is failed, connected is not ready.")
        if not self.server_lock.acquire(timeout=timeout):  # wait trigger lock is unlocked
            raise ReceiveTimeoutError("Client receive data timeout: %s", timeout)
        # logger.debug("Client sended return data: %s" % str(self.server_data))
        return self.server_data

    def process_event(self, value):
        # logger.debug("Client process event starting %s" % str(value))
        self.server_data = value
        if self.server_lock.locked():
            self.server_lock.release()
        logger.debug("Client process event ended")


if __name__ == "__main__":
    from twisted.internet import reactor
    host = '127.0.0.1'
    port = 60000
    client = ControllerClientFactory()
    reactor.connectTCP(host, port, client)
    reactor.run()
