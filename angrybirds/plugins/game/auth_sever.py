#!/usr/bin/env python3
""" Auth Server class for plane simuation exe"""
import logging
import datetime
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
logger = logging.getLogger(__name__)
auth_dict = {
    '05/01/2020': b'\xcd\xb9\x00\x00',
    '05/02/2020': b'\xdb\xbc\x00\x00',
    '05/03/2020': b'\xc8\xc7\x00\x00',
    '05/04/2020': b'\xcd\xc6\x00\x00',
    '05/05/2020': b'\xb1\xce\x00\x00',
    '05/06/2020': b'\xc4\xbd\x00\x00',
    '05/07/2020': b'\xc7\xd9\x00\x00',
    '05/08/2020': b'\xcd\xb9\x00\x00',
    '05/09/2020': b'\xdb\xbc\x00\x00',
    '05/10/2020': b'\xc8\xc7\x00\x00',
    '05/11/2020': b'\xcd\xc6\x00\x00',
    '05/12/2020': b'\xb1\xce\x00\x00',
    '05/13/2020': b'\xc4\xbd\x00\x00',
    '05/14/2020': b'\xc7\xd9\x00\x00',
    '05/15/2020': b'\xcd\xb9\x00\x00',
    '05/16/2020': b'\xdb\xbc\x00\x00',
    '05/17/2020': b'\xc8\xc7\x00\x00',
    '05/18/2020': b'\xcd\xc6\x00\x00',
    '05/19/2020': b'\xb1\xce\x00\x00',
    '05/20/2020': b'\xc4\xbd\x00\x00',
    '05/21/2020': b'\xc7\xd9\x00\x00',
    '05/22/2020': b'\xcd\xb9\x00\x00',
    '05/23/2020': b'\xdb\xbc\x00\x00',
    '05/24/2020': b'\xc8\xc7\x00\x00',
    '05/25/2020': b'\xcd\xc6\x00\x00',
    '05/26/2020': b'\xb1\xce\x00\x00',
    '05/27/2020': b'\xc4\xbd\x00\x00',
    '05/28/2020': b'\xc7\xd9\x00\x00',
    '05/29/2020': b'\xcd\xb9\x00\x00',
    '05/30/2020': b'\xdb\xbc\x00\x00',
    '05/31/2020': b'\xc8\xc7\x00\x00',
    '06/01/2020': b'\xda\xd2\x00\x00',
    '06/02/2020': b'\xeb\xbf\x00\x00',
    '06/03/2020': b'\xf3\xbc\x00\x00',
    '06/04/2020': b'\xcf\xd9\x00\x00',
    '06/05/2020': b'\xb1\xd9\x00\x00',
    '06/06/2020': b'\xad\xd9\x00\x00',
    '06/07/2020': b'\xaf\xd9\x00\x00',
    '06/08/2020': b'\xda\xd2\x00\x00',
    '06/09/2020': b'\xeb\xbf\x00\x00',
    '06/10/2020': b'\xf3\xbc\x00\x00',
    '06/11/2020': b'\xcf\xd9\x00\x00',
    '06/12/2020': b'\xb1\xd9\x00\x00',
    '06/13/2020': b'\xad\xd9\x00\x00',
    '06/14/2020': b'\xaf\xd9\x00\x00',
    '06/15/2020': b'\xda\xd2\x00\x00',
    '06/16/2020': b'\xeb\xbf\x00\x00',
    '06/17/2020': b'\xf3\xbc\x00\x00',
    '06/18/2020': b'\xcf\xd9\x00\x00',
    '06/19/2020': b'\xb1\xd9\x00\x00',
    '06/20/2020': b'\xad\xd9\x00\x00',
    '06/21/2020': b'\xaf\xd9\x00\x00',
    '06/22/2020': b'\xda\xd2\x00\x00',
    '06/23/2020': b'\xeb\xbf\x00\x00',
    '06/24/2020': b'\xf3\xbc\x00\x00',
    '06/25/2020': b'\xcf\xd9\x00\x00',
    '06/26/2020': b'\xb1\xd9\x00\x00',
    '06/27/2020': b'\xad\xd9\x00\x00',
    '06/28/2020': b'\xaf\xd9\x00\x00',
    '06/29/2020': b'\xda\xd2\x00\x00',
    '06/30/2020': b'\xeb\xbf\x00\x00',
    '07/01/2020': b'\xb3\xd9\x00\x00',
    '07/02/2020': b'\xd0\xd9\x00\x00',
    '07/03/2020': b'\xce\xd9\x00\x00',
    '07/04/2020': b'\xb2\xd9\x00\x00',
    '07/05/2020': b'\xa5\xb3\x00\x00',
    '07/06/2020': b'\xc5\xd3\x00\x00',
    '07/07/2020': b'\xa2\xb4\x00\x00',
    '07/08/2020': b'\xb3\xd9\x00\x00',
    '07/09/2020': b'\xd0\xd9\x00\x00',
    '07/10/2020': b'\xce\xd9\x00\x00',
    '07/11/2020': b'\xb2\xd9\x00\x00',
    '07/12/2020': b'\xa5\xb3\x00\x00',
    '07/13/2020': b'\xc5\xd3\x00\x00',
    '07/14/2020': b'\xa2\xb4\x00\x00',
    '07/15/2020': b'\xb3\xd9\x00\x00',
    '07/16/2020': b'\xd0\xd9\x00\x00',
    '07/17/2020': b'\xce\xd9\x00\x00',
    '07/18/2020': b'\xb2\xd9\x00\x00',
    '07/19/2020': b'\xa5\xb3\x00\x00',
    '07/20/2020': b'\xc5\xd3\x00\x00',
    '07/21/2020': b'\xa2\xb4\x00\x00',
    '07/22/2020': b'\xb3\xd9\x00\x00',
    '07/23/2020': b'\xd0\xd9\x00\x00',
    '07/24/2020': b'\xce\xd9\x00\x00',
    '07/25/2020': b'\xb2\xd9\x00\x00',
    '07/26/2020': b'\xa5\xb3\x00\x00',
    '07/27/2020': b'\xc5\xd3\x00\x00',
    '07/28/2020': b'\xa2\xb4\x00\x00',
    '07/29/2020': b'\xb3\xd9\x00\x00',
    '07/30/2020': b'\xd0\xd9\x00\x00',
    '07/31/2020': b'\xce\xd9\x00\x00',
    '08/01/2020': b'\xf2\xd4\x00\x00',
    '08/02/2020': b'\xf9\xb6\x00\x00',
    '08/03/2020': b'\xbd\xc1\x00\x00',
    '08/04/2020': b'\xe1\xb2\x00\x00',
    '08/05/2020': b'\xb3\xb6\x00\x00',
    '08/06/2020': b'\xad\xbf\x00\x00',
    '08/07/2020': b'\xd9\xd8\x00\x00',
    '08/08/2020': b'\xf2\xd4\x00\x00',
    '08/09/2020': b'\xf9\xb6\x00\x00',
    '08/10/2020': b'\xbd\xc1\x00\x00',
    '08/11/2020': b'\xe1\xb2\x00\x00',
    '08/12/2020': b'\xb3\xb6\x00\x00',
    '08/13/2020': b'\xad\xbf\x00\x00',
    '08/14/2020': b'\xd9\xd8\x00\x00',
    '08/15/2020': b'\xf2\xd4\x00\x00',
    '08/16/2020': b'\xf9\xb6\x00\x00',
    '08/17/2020': b'\xbd\xc1\x00\x00',
    '08/18/2020': b'\xe1\xb2\x00\x00',
    '08/19/2020': b'\xb3\xb6\x00\x00',
    '08/20/2020': b'\xad\xbf\x00\x00',
    '08/21/2020': b'\xd9\xd8\x00\x00',
    '08/22/2020': b'\xf2\xd4\x00\x00',
    '08/23/2020': b'\xf9\xb6\x00\x00',
    '08/24/2020': b'\xbd\xc1\x00\x00',
    '08/25/2020': b'\xe1\xb2\x00\x00',
    '08/26/2020': b'\xb3\xb6\x00\x00',
    '08/27/2020': b'\xad\xbf\x00\x00',
    '08/28/2020': b'\xd9\xd8\x00\x00',
    '08/29/2020': b'\xf2\xd4\x00\x00',
    '08/30/2020': b'\xf9\xb6\x00\x00',
    '08/31/2020': b'\xbd\xc1\x00\x00',
    '09/01/2020': b'\xfd\xd4\x00\x00',
    '09/02/2020': b'\xdc\xd8\x00\x00',
    '09/03/2020': b'\xb4\xb4\x00\x00',
    '09/04/2020': b'\xf9\xb2\x00\x00',
    '09/05/2020': b'\xae\xbb\x00\x00',
    '09/06/2020': b'\xd5\xb8\x00\x00',
    '09/07/2020': b'\xd0\xb9\x00\x00',
    '09/08/2020': b'\xfd\xd4\x00\x00',
    '09/09/2020': b'\xdc\xd8\x00\x00',
    '09/10/2020': b'\xb4\xb4\x00\x00',
    '09/11/2020': b'\xf9\xb2\x00\x00',
    '09/12/2020': b'\xae\xbb\x00\x00',
    '09/13/2020': b'\xd5\xb8\x00\x00',
    '09/14/2020': b'\xd0\xb9\x00\x00',
    '09/15/2020': b'\xfd\xd4\x00\x00',
    '09/16/2020': b'\xdc\xd8\x00\x00',
    '09/17/2020': b'\xb4\xb4\x00\x00',
    '09/18/2020': b'\xf9\xb2\x00\x00',
    '09/19/2020': b'\xae\xbb\x00\x00',
    '09/20/2020': b'\xd5\xb8\x00\x00',
    '09/21/2020': b'\xd0\xb9\x00\x00',
    '09/22/2020': b'\xfd\xd4\x00\x00',
    '09/23/2020': b'\xdc\xd8\x00\x00',
    '09/24/2020': b'\xb4\xb4\x00\x00',
    '09/25/2020': b'\xf9\xb2\x00\x00',
    '09/26/2020': b'\xae\xbb\x00\x00',
    '09/27/2020': b'\xd5\xb8\x00\x00',
    '09/28/2020': b'\xd0\xb9\x00\x00',
    '09/29/2020': b'\xfd\xd4\x00\x00',
    '09/30/2020': b'\xdc\xd8\x00\x00',
    '10/01/2020': b'\xa3\xbd\x00\x00',
    '10/02/2020': b'\xc1\xbc\x00\x00',
    '10/03/2020': b'\xa2\xbe\x00\x00',
    '10/04/2020': b'\xe7\xbe\x00\x00',
    '10/05/2020': b'\xf5\xc1\x00\x00',
    '10/06/2020': b'\xf4\xb9\x00\x00',
    '10/07/2020': b'\xdb\xd8\x00\x00',
    '10/08/2020': b'\xa3\xbd\x00\x00',
    '10/09/2020': b'\xc1\xbc\x00\x00',
    '10/10/2020': b'\xa2\xbe\x00\x00',
    '10/11/2020': b'\xe7\xbe\x00\x00',
    '10/12/2020': b'\xf5\xc1\x00\x00',
    '10/13/2020': b'\xf4\xb9\x00\x00',
    '10/14/2020': b'\xdb\xd8\x00\x00',
    '10/15/2020': b'\xa3\xbd\x00\x00',
    '10/16/2020': b'\xc1\xbc\x00\x00',
    '10/17/2020': b'\xa2\xbe\x00\x00',
    '10/18/2020': b'\xe7\xbe\x00\x00',
    '10/19/2020': b'\xf5\xc1\x00\x00',
    '10/20/2020': b'\xf4\xb9\x00\x00',
    '10/21/2020': b'\xdb\xd8\x00\x00',
    '10/22/2020': b'\xa3\xbd\x00\x00',
    '10/23/2020': b'\xc1\xbc\x00\x00',
    '10/24/2020': b'\xa2\xbe\x00\x00',
    '10/25/2020': b'\xe7\xbe\x00\x00',
    '10/26/2020': b'\xf5\xc1\x00\x00',
    '10/27/2020': b'\xf4\xb9\x00\x00',
    '10/28/2020': b'\xdb\xd8\x00\x00',
    '10/29/2020': b'\xa3\xbd\x00\x00',
    '10/30/2020': b'\xc1\xbc\x00\x00',
    '10/31/2020': b'\xa2\xbe\x00\x00',
    '11/01/2020': b'\xf1\xce\x00\x00',
    '11/02/2020': b'\xab\xd1\x00\x00',
    '11/03/2020': b'\xa4\xca\x00\x00',
    '11/04/2020': b'\xcd\xc0\x00\x00',
    '11/05/2020': b'\xc6\xca\x00\x00',
    '11/06/2020': b'\xd6\x84\x00\x00',
    '11/07/2020': b'\xf8\xc0\x00\x00',
    '11/08/2020': b'\xf1\xce\x00\x00',
    '11/09/2020': b'\xab\xd1\x00\x00',
    '11/10/2020': b'\xa4\xca\x00\x00',
    '11/11/2020': b'\xcd\xc0\x00\x00',
    '11/12/2020': b'\xc6\xca\x00\x00',
    '11/13/2020': b'\xd6\x84\x00\x00',
    '11/14/2020': b'\xf8\xc0\x00\x00',
    '11/15/2020': b'\xf1\xce\x00\x00',
    '11/16/2020': b'\xab\xd1\x00\x00',
    '11/17/2020': b'\xa4\xca\x00\x00',
    '11/18/2020': b'\xcd\xc0\x00\x00',
    '11/19/2020': b'\xc6\xca\x00\x00',
    '11/20/2020': b'\xd6\x84\x00\x00',
    '11/21/2020': b'\xf8\xc0\x00\x00',
    '11/22/2020': b'\xf1\xce\x00\x00',
    '11/23/2020': b'\xab\xd1\x00\x00',
    '11/24/2020': b'\xa4\xca\x00\x00',
    '11/25/2020': b'\xcd\xc0\x00\x00',
    '11/26/2020': b'\xc6\xca\x00\x00',
    '11/27/2020': b'\xd6\x84\x00\x00',
    '11/28/2020': b'\xf8\xc0\x00\x00',
    '11/29/2020': b'\xf1\xce\x00\x00',
    '11/30/2020': b'\xab\xd1\x00\x00',
    '12/01/2020': b'\xd1\xd8\x00\x00',
    '12/02/2020': b'\xf8\xc7\x00\x00',
    '12/03/2020': b'\xad\xd0\x00\x00',
    '12/04/2020': b'\xc7\xd8\x00\x00',
    '12/05/2020': b'\xe1\xd1\x00\x00',
    '12/06/2020': b'\xd0\xd8\x00\x00',
    '12/07/2020': b'\xe3\xbb\x00\x00',
    '12/08/2020': b'\xd1\xd8\x00\x00',
    '12/09/2020': b'\xf8\xc7\x00\x00',
    '12/10/2020': b'\xad\xd0\x00\x00',
    '12/11/2020': b'\xc7\xd8\x00\x00',
    '12/12/2020': b'\xe1\xd1\x00\x00',
    '12/13/2020': b'\xd0\xd8\x00\x00',
    '12/14/2020': b'\xe3\xbb\x00\x00',
    '12/15/2020': b'\xd1\xd8\x00\x00',
    '12/16/2020': b'\xf8\xc7\x00\x00',
    '12/17/2020': b'\xad\xd0\x00\x00',
    '12/18/2020': b'\xc7\xd8\x00\x00',
    '12/19/2020': b'\xe1\xd1\x00\x00',
    '12/20/2020': b'\xd0\xd8\x00\x00',
    '12/21/2020': b'\xe3\xbb\x00\x00',
    '12/22/2020': b'\xd1\xd8\x00\x00',
    '12/23/2020': b'\xf8\xc7\x00\x00',
    '12/24/2020': b'\xad\xd0\x00\x00',
    '12/25/2020': b'\xc7\xd8\x00\x00',
    '12/26/2020': b'\xe1\xd1\x00\x00',
    '12/27/2020': b'\xd0\xd8\x00\x00',
    '12/28/2020': b'\xe3\xbb\x00\x00',
    '12/29/2020': b'\xd1\xd8\x00\x00',
}


class AuthServer(Protocol):

    def __init__(self, factory):
        logger.debug("Initializing %s" % self.__class__.__name__)
        self.factory = factory
        logger.debug("Initialized %s" % self.__class__.__name__)

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.factory.addClient(self)
        self.dataSend(self.factory.initData())
        logger.debug("AuthServer new connect: %d" % (self.factory.numProtocols))

    def connectionLost(self, reason):
        logger.debug("AuthServer lost connect: %d %s" % (self.factory.numProtocols, reason))
        self.factory.numProtocols = self.factory.numProtocols - 1
        self.factory.delClient(self)

    def dataReceived(self, data):
        pass

    def dataSend(self, data: bytes):
        self.transport.write(data)


class AuthServerFactory(Factory):

    def __init__(self):
        logger.debug("Initializing %s" % self.__class__.__name__)
        self.numProtocols = 0
        self.clients = []
        logger.debug("Initialized %s" % self.__class__.__name__)

    def buildProtocol(self, addr):
        logger.debug("AuthServer has Client Connected")
        return AuthServer(self)

    def addClient(self, client):
        logger.debug("AuthServer append Client to list")
        self.clients.append(client)

    def delClient(self, client):
        logger.debug("AuthServer delete Client from list")
        self.clients.remove(client)

    def initData(self):
        now = datetime.datetime.utcnow()
        date = now.strftime("%m/%d/%Y")
        return auth_dict.get(date, b'\x00\x00\x00\x00')

if __name__ == "__main__":
    from twisted.internet import reactor
    factory = AuthServerFactory()
    factory2 = AuthServerFactory()
    endpoint = TCP4ServerEndpoint(reactor=reactor, port=12345, interface='127.0.0.1')
    endpoint2 = TCP4ServerEndpoint(reactor=reactor, port=12346, interface='127.0.0.1')
    endpoint.listen(factory)
    endpoint2.listen(factory2)
    import threading
    mthread = threading.Thread(target=reactor.run, args=(False,))
    mthread.setDaemon(True)
    mthread.start()
    mthread.join()
