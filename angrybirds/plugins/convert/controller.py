#!/usr/bin/env python3
"""  Parent Class for Controller command"""

import logging
import struct
from enum import Enum
from angrybirds.config.plane_config import EnvConfig
from angrybirds.config.plane_config import RequestMsgID
from angrybirds.config.plane_config import ResponseMsgID
from angrybirds.config.plane_config import ResponseMsgCode
from angrybirds.config.plane_config import RedPlane
from angrybirds.config.plane_config import BluePlane
from angrybirds.lib.watchdog import Watchdog
from angrybirds.lib.error import ReceiveTimeoutError, CheckResponseError
from angrybirds.config.sim_env_config import PluginExeControlTimeout
logger = logging.getLogger(__name__)


def encode_msg_type(value: Enum) -> bytes:
    return struct.pack('<B', value.value)


def encode_msg_data(cls: object) -> bytes:
    data = b''
    fields = getattr(cls, '_fields_', [])
    for fmt, fieldname in fields:
        data += struct.pack('<' + fmt, getattr(cls, fieldname))
    return data


def decode_msg(response: bytes) -> tuple:
    return struct.unpack('<BB', response)


class Controller:

    def __init__(self, client, timeout=PluginExeControlTimeout):
        logger.debug("Initializing %s", self.__class__.__name__)
        self.client = client
        self.watchdog = Watchdog(timeout=timeout, userHandler=self.Handler, name='Controller')
        self.timeout = timeout
        self.istimeout = False
        logger.debug("Initialized %s", self.__class__.__name__)

    def check(self, request_code: Enum, response: bytes) -> bool:
        error_code, error_msg = decode_msg(response)
        error_describe = ResponseMsgCode.Code.get(error_msg, "未知错误")
        logger.debug("Controller {} response: {}".format(request_code.name, error_describe))
        auth_code = getattr(ResponseMsgID, request_code.name, -1)
        if auth_code.value != error_code:
            raise CheckResponseError("Controller send:{} response:{},{}".format(
                auth_code.name, ResponseMsgID(error_code), error_describe))

    def Handler(self):
        self.istimeout = True
        self.watchdog.stop()

    def resetTimeout(self):
        self.watchdog.reset()
        self.istimeout = False

    def send(self, data: bytes, non_blocked=False):
        self.resetTimeout()
        while not self.client.protocol or not self.client.protocol.connected:
            if self.istimeout:
                raise ReceiveTimeoutError("Controller client connection server timeout")
        self.watchdog.stop()
        return self.client.send(data, timeout=self.timeout, non_blocked=non_blocked)

    def scenario(self):
        request_code = RequestMsgID.SCENARIO
        logger.debug("Controller {} send code: {}".format(request_code.name, request_code.value))
        data = encode_msg_type(request_code)
        data += encode_msg_data(EnvConfig)
        data += encode_msg_data(RedPlane)
        data += encode_msg_data(BluePlane)
        response = self.send(data)
        self.check(request_code, response)

    def init(self):
        request_code = RequestMsgID.INIT
        logger.debug("Controller {} send code: {}".format(request_code.name, request_code.value))
        data = encode_msg_type(request_code)
        response = self.send(data)
        self.check(request_code, response)

    def start(self):
        request_code = RequestMsgID.START
        logger.debug("Controller {} send code: {}".format(request_code.name, request_code.value))
        data = encode_msg_type(request_code)
        response = self.send(data)
        self.check(request_code, response)

    def pause(self, non_blocked=False):
        request_code = RequestMsgID.PAUSE
        logger.debug("Controller {} send code: {}".format(request_code.name, request_code.value))
        data = encode_msg_type(request_code)
        response = self.send(data, non_blocked=non_blocked)
        if not non_blocked:
            self.check(request_code, response)

    def stop(self):
        request_code = RequestMsgID.STOP
        logger.debug("Controller {} send code: {}".format(request_code.name, request_code.value))
        data = encode_msg_type(request_code)
        response = self.send(data)
        self.check(request_code, response)
