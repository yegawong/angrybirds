#!/usr/bin/env python3
""" Exception Errors available across all scripts """


class DecodePacketError(Exception):
    """ Decode Packet Error for handling specific errors with useful information """
    pass


class ReceiveTimeoutError(Exception):
    """ Receive Packet Time out Error for Server and Client """
    pass


class ClientConnectError(Exception):
    """ Client not connected"""
    pass


class ServerConnectClientError(Exception):
    """ Server have Client shortage in number """
    pass


class DeferredCallbackError(Exception):
    """ Deferred Object Callback Error """
    pass


class QtNotFoundError(Exception):
    """ Not Found Qt Software """
    pass


class QtVersionError(Exception):
    """ Qt Outdated Version """
    pass


class FlagTxtCreateError(Exception):
    """ plugin exe create txt file failed """
    pass


class CheckResponseError(Exception):
    """ send data return response result Incorrect """
    pass


class StartExeError(Exception):
    """ start exe failed """
    pass


class ExeError(Exception):
    """ execute exe failed """
    pass


class ConvertVauleError(Exception):
    """ Vaule has nan/inf """
    pass
