from ctypes import Array, Structure
from angrybirds.plugins.convert.plane_situation import AIData as angrybirds_AIData
from angrybirds.plugins.convert.plane_action import AIInputData as angrybirds_AIInputData
from angrybirds.plugins.convert.plane_action import AIIputDataDefaultValue as angrybirds_AIIputDataDefaultValue
from angrybirds.plugins.opponent.plane_situation_opponent import AIData as opponent_AIData
from angrybirds.plugins.opponent.plane_action_opponent import AIInputData as opponent_AIInputData
from angrybirds.lib.error import ConvertVauleError
import math
import logging
logger = logging.getLogger(__name__)


def generate_angrybirds_aiiputdata() -> angrybirds_AIInputData:
    """[use zero and default value generate AI to simulation structure]

    Returns:
        AIInputData -- [AI to simulation structure object]
    """
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


def iter_assign(target, src, isaction=False):
    fields = getattr(src, '_fields_', [])
    if isaction:
        fields = getattr(target, '_fields_', [])
    for fmt, fieldname in fields:
        if hasattr(target, fieldname):
            status = getattr(target, fieldname)
            if isinstance(status, Structure) or isinstance(status, Array):
                break
            value = getattr(src, fieldname)
            if math.isnan(value) or math.isinf(value):   # outlier detection
                logger.error("{} is error, value is: {}".format(fieldname, value))
                # raise ConvertVauleError("{} is error, value is: {}".format(fieldname, value))
            setattr(target, fieldname, value)
        else:
            res = fieldname.split('_')
            if len(res) == 2 and res[1].isdigit():
                value = getattr(src, fieldname)
                tmp = getattr(target, res[0])
                tmp[int(res[1])] = value
            else:
                raise ValueError(target, "no have", fieldname)


def situation_to_opponent_situation(situation: angrybirds_AIData):
    """
    :param situation: simulator situation of angrybirds interface
    :return: opponent situation interface
    """
    rule_input = opponent_AIData()
    rule_input.AATargetDataListNum = situation.AATargetDataListNum
    for i in range(rule_input.AATargetDataListNum):
        iter_assign(rule_input.sAATargetData[i], situation.sAATargetData[i])
    iter_assign(rule_input.sSMSData, situation.sSMSData)
    iter_assign(rule_input.sFCMData, situation.sFCMData)
    iter_assign(rule_input.sFCMData.sFCMRDM, situation.sFCMData.sFCMRDM)
    iter_assign(rule_input.sFCMData.sFCMIRM, situation.sFCMData.sFCMIRM)
    rule_input.nMslPropertyNum = situation.nMslPropertyNum
    for i in range(rule_input.nMslPropertyNum):
        iter_assign(rule_input.sMslProperty[i], situation.sMslProperty[i])
    iter_assign(rule_input.sStateData, situation.sStateData)
    rule_input.nAIMInfoInfoNum = situation.nAIMInfoInfoNum
    for i in range(rule_input.nAIMInfoInfoNum):
        iter_assign(rule_input.sAIMInfo, situation.sAIMInfo)
    rule_input.sAttackList.nTargetInListNum = situation.nTargetInListNum
    for i in range(rule_input.sAttackList.nTargetInListNum):
        iter_assign(rule_input.sAttackList.sTargetInListData[i], situation.sTargetInListData[i])
    iter_assign(rule_input.sFighterPara, situation.sFighterPara)
    iter_assign(rule_input.sOtherInfo, situation.sOtherInfo)
    if situation.nAlarmNum > 10:
        logger.error("situation.nAlarmNum is {}, now is 10".format(situation.nAlarmNum))
        situation.nAlarmNum = 10
    rule_input.sOtherInfo.nAlarmNum = situation.nAlarmNum
    for i in range(rule_input.sOtherInfo.nAlarmNum):
        iter_assign(rule_input.sOtherInfo.sAlarm[i], situation.sAlarm[i])
    iter_assign(rule_input.sOtherInfo, situation.stherInfoSub)
    return rule_input


def opponent_action_to_action(rule_output: opponent_AIInputData):
    """
    :param situation: simulator situation of angrybirds interface
    :return: opponent situation interface
    """
    action = generate_angrybirds_aiiputdata()
    fields = getattr(action, '_fields_', [])
    for fmt, fieldname in fields:
        target = getattr(action, fieldname)
        src = getattr(rule_output, fieldname)
        iter_assign(target, src, isaction=True)
    return action
