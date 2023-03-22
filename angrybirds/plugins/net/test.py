from server import DataInterfaceFactory
from client import ControllerClientFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
import threading
import struct


class Controller:

    def __init__(self, client):
        self.client = client

    def scenario(self):
        type_ = 0
        beat_ = 60
        record_ = 1
        situation_ = 1
        log_ = 1
        cloud_ = 0
        rain_ = 0
        fog_ = 0
        count_ = 2
        data = struct.pack('BBBBBBBBB', type_, beat_, record_, situation_, log_, cloud_, rain_,
                           fog_, count_)
        longitude = 115.0
        latitude = 30.4
        height = 6000.0
        heading = 0.0
        speed = 240.0
        fuel = 3000.0
        dis_per = 100
        data += struct.pack('<ddddddB', longitude, latitude, height, heading, speed, fuel, dis_per)

        longitude = 115.0
        latitude = 30.6
        height = 6000.0
        heading = 180.0
        speed = 240.0
        fuel = 3000.0
        dis_per = 100
        data += struct.pack('<ddddddB', longitude, latitude, height, heading, speed, fuel, dis_per)
        response = self.client.send(data)
        print('scenario response', response)

    def init(self):
        data = struct.pack('B', 2)
        response = self.client.send(data)
        print('init response', response)

    def start(self):
        data = struct.pack('B', 4)
        response = self.client.send(data)
        print('start response', response)

    def pause(self):
        data = struct.pack('B', 6)
        response = self.client.send(data)
        print('pause response', response)

    def continued(self):
        data = struct.pack('B', 8)
        response = self.client.send(data)
        print('continued response', response)

    def stop(self):
        data = struct.pack('B', 10)
        response = self.client.send(data)
        print('stop response', response)

    def heartbeat(self):
        data = struct.pack('B', 12)
        response = self.client.send(data, non_blocked=True)
        print('heartbeat response', response)


aiinputdata = b'\x03\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
control_port = 60000
data_port = 60001
host = '127.0.0.1'

from twisted.internet import reactor
data_service = DataInterfaceFactory(client_cnt=2)
endpoint = TCP4ServerEndpoint(reactor=reactor, port=data_port, interface=host)
endpoint.listen(data_service)
controller = ControllerClientFactory()
reactor.connectTCP(host, control_port, controller)
mthread = threading.Thread(target=reactor.run,
                           args=(False,))  # kwargs={'installSignalHandlers': False})
mthread.start()
print(mthread.isAlive())
while not controller.protocol or not controller.protocol.connected:
    pass
try:
    controller = Controller(controller)
    controller.scenario()
    controller.init()
    controller.start()
    print("client done")
    data = data_service.initData()
    print('data', len(data))
    print(data)
    data = data_service.sendAll([aiinputdata] * 2)
    print('data', len(data))
    # while True:
    #     controller.heartbeat()

except KeyboardInterrupt:
    print("except")
finally:
    reactor.stop()
