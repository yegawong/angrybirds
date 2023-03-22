from ctypes import Array, Structure
from angrybirds.plugins.opponent.plane_situation_opponent_kf import AIData as kf_AIData
from angrybirds.plugins.opponent.plane_action_opponent_kf import AIInputData as kf_AIInputData
from angrybirds.plugins.opponent.plane_situation_opponent import AIData as gbz_AIData
from angrybirds.plugins.opponent.plane_action_opponent import AIInputData as gbz_AIInputData
import logging
logger = logging.getLogger(__name__)


def iter_assign(target, src, isaction=False):
    fields = getattr(target, '_fields_', [])
    if isaction:
        fields = getattr(src, '_fields_', [])
    for fieldname, fmt in fields:
        if issubclass(fmt, Structure) or issubclass(fmt, Array):
            continue
        value = getattr(src, fieldname, None)
        if value is None:
            continue
        setattr(target, fieldname, value)


def gbzsituation_to_kfsituation(situation: gbz_AIData):
    """
    :param situation: simulator situation of angrybirds interface
    :return: opponent situation interface
    """
    rule_input = kf_AIData()
    rule_input.AATargetDataListNum = situation.AATargetDataListNum
    for i in range(rule_input.AATargetDataListNum):
        iter_assign(rule_input.sAATargetData[i], situation.sAATargetData[i])
    iter_assign(rule_input.sSMSData, situation.sSMSData)
    iter_assign(rule_input.sFCMData, situation.sFCMData)
    iter_assign(rule_input.sFCMData.sFCMRDM, situation.sFCMData.sFCMRDM)
    iter_assign(rule_input.sFCMData.sFCMIRM, situation.sFCMData.sFCMIRM)
    rule_input.sFCMData.nMslPropertyNum = situation.nMslPropertyNum
    for i in range(rule_input.sFCMData.nMslPropertyNum):
        iter_assign(rule_input.sFCMData.sMslProperty[i], situation.sMslProperty[i])
    iter_assign(rule_input.sStateData, situation.sStateData)
    rule_input.nAIMInfoInfoNum = situation.nAIMInfoInfoNum
    for i in range(rule_input.nAIMInfoInfoNum):
        iter_assign(rule_input.sAIMInfo, situation.sAIMInfo)
    rule_input.sAttackList.nTargetInListNum = situation.sAttackList.nTargetInListNum
    for i in range(rule_input.sAttackList.nTargetInListNum):
        iter_assign(rule_input.sAttackList.sTargetInListData[i], situation.sAttackList.sTargetInListData[i])
    iter_assign(rule_input.sFighterPara, situation.sFighterPara)
    iter_assign(rule_input.sOtherInfo, situation.sOtherInfo)
    rule_input.sOtherInfo.nAlarmNum = situation.sOtherInfo.nAlarmNum
    for i in range(rule_input.sOtherInfo.nAlarmNum):
        iter_assign(rule_input.sOtherInfo.sAlarm[i], situation.sOtherInfo.sAlarm[i])
    return rule_input


def kfaction_to_gbzaction(rule_output: kf_AIData):
    """
    :param situation: simulator situation of angrybirds interface
    :return: opponent situation interface
    """
    action = gbz_AIInputData()
    fields = getattr(action, '_fields_', [])
    for fieldname, fmt in fields:
        target = getattr(action, fieldname)
        src = getattr(rule_output, fieldname)
        iter_assign(target, src, isaction=True)
    return action
