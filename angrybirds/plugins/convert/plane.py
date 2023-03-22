#!/usr/bin/env python3
""" Parent class for plane data interaction proto stream converter """
from angrybirds.plugins.convert.plane_situation import AIData
from angrybirds.lib.structure import StructureMeta, SizedRecord
from angrybirds.lib.error import DecodePacketError
from angrybirds.plugins.convert.plane_situation import AIData as angrybirds_AIData
from angrybirds.plugins.convert.plane_action import AIInputData as angrybirds_AIInputData
from angrybirds.plugins.convert.plane_action import AIIputDataDefaultValue as angrybirds_AIIputDataDefaultValue
from angrybirds.plugins.opponent.convert import situation_to_opponent_situation
from angrybirds.plugins.opponent.convert import opponent_action_to_action
from angrybirds.plugins.opponent.plane_action_opponent import AIInputData as opponent_AIInputData
import logging
logger = logging.getLogger(__name__)


class BridCoder:
    """Parent class for plane"""

    def __init__(self):
        logger.debug("Initializing %s", self.__class__.__name__)
        self.__aiinputdata = None
        self.__aidata = None
        logger.debug("Initialized %s", self.__class__.__name__)

    def generate_aiiputdata(self) -> angrybirds_AIInputData:
        """[use zero and default value generate AI to simulation structure]

        Returns:
            AIInputData -- [AI to simulation structure object]
        """
        # @TODO
        # return opponent_AIInputData()  # No initial value, All zero, Temporary abandoning
        logger.debug("Starting generate AIInputData")
        none_data = b'\x00' * angrybirds_AIInputData.struct_size
        aiinputdata = angrybirds_AIInputData(none_data)
        default_value = angrybirds_AIIputDataDefaultValue.default_value
        for key, value in default_value.items():
            if isinstance(value, dict):
                for sub_key, sub_v in value.items():
                    fieldname = getattr(aiinputdata, key)
                    setattr(fieldname, sub_key, sub_v)
            else:
                setattr(aiinputdata, key, value)
        logger.debug("Started generate AIInputData")
        return aiinputdata

    def encode_aiiputdata(self, action) -> bytes:
        if isinstance(action, opponent_AIInputData):
            action = opponent_action_to_action(action) # No initial value, All zero, Temporary abandoning
        return action.encode_data()

    def decode_aidata(self, data: bytes) -> AIData:
        """[read bytes stream data decode to structure object]

        Arguments:
            data {bytes} -- [simulation to AI byte stream]

        Returns:
            AIData -- [simulation to AI structure object]
        """
        logger.debug("Starting decode AIData")
        aidata = AIData(b'')
        fields = getattr(aidata, '_fields_', [])
        ranges = getattr(aidata, '_ranges_', [])
        offest = 0
        num = 0
        repeat = False

        for fmt, fieldname in fields:
            if isinstance(fmt, StructureMeta):
                if repeat:
                    rec = SizedRecord(data[offest:])
                    setattr(aidata, fieldname, [attr for attr in rec.iter_as(fmt, num)])
                    offest += num * fmt.struct_size
                else:
                    rec = SizedRecord(data[offest:])
                    setattr(aidata, fieldname, [attr for attr in rec.iter_as(fmt, 1)][0])
                    offest += fmt.struct_size
                num = 0
                repeat = False
            else:
                rec = SizedRecord(data[offest:])
                size, num = rec.unpack_num(fmt)
                min_r, max_r = ranges.get(fieldname, (0, 0))
                if min_r > num or max_r < num:
                    raise DecodePacketError(
                        "{} is {}, min:{}, max:{}, AIData bytes length:{}".format(
                            fieldname, num, min_r, max_r, len(data)))
                repeat = True
                setattr(aidata, fieldname, num)
                offest += size
        self.__aidata = aidata
        logger.debug("Started decode AIData")
        return situation_to_opponent_situation(self.__aidata)
