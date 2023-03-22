#!/usr/bin/python
""" EarlPig Decode Function """
import math
from ctypes import (
    Structure,
    POINTER,
    cdll,
    Array,
    byref,
    c_bool,
    c_int,
    c_float,
    c_double,
    c_short,
    c_ushort,
)
from .plane_situation_model import *


class AATargetInfo(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("nAllyLot", c_int),
        ("nAELot", c_int),
        ("nOELot", c_int),
        ("nEWLot", c_int),
        ("nDLLot", c_int),
        ("nPlatformnIdentify", c_int),
        ("bNTS", c_bool),
        ("nPrecisionType", c_int),
        ("nIdentification", c_int),
        ("nOESAWorkState", c_int),
        ("nAESAWorkState", c_int),
        ("bAETarget", c_bool),
        ("bOETarget", c_bool),
        ("bEWTarget", c_bool),
        ("bDLTarget", c_bool),
        ("nJamDegree", c_int),
        ("nIdentify", c_int),
        ("nIdentifyResults", c_int),
        ("nIdentifyAttackResults", c_int),
        ("nFormationTypes", c_int),
        ("fTargetDistanceDF_m", c_float),
        ("fDisAlterRateDF_ms", c_float),
        ("fTargetAzimDF_rad", c_float),
        ("fTargetPitchDF_rad", c_float),
        ("fTargetAzimVelGDF_rads", c_float),
        ("fTargetPitchVelGDF_rads", c_float),
        ("fVnDF_ms", c_float),
        ("fVuDF_ms", c_float),
        ("fVeDF_ms", c_float),
        ("fAccNDF_ms2", c_float),
        ("fAccUDF_ms2", c_float),
        ("fAccEDF_ms2", c_float),
        ("fDisPrecisionDF_m", c_float),
        ("fDisRatePrecisionDF_ms", c_float),
        ("fAzimPrecisionBDF_mrad", c_float),
        ("fPitchPrecisionDF_mrad", c_float),
        ("fAzhimRatePcsnBDF_mrads", c_float),
        ("fPitchRatePcsnBDF_mrads", c_float),
        ("fVnPcsnDF_ms", c_float),
        ("fVePcsnDF_ms", c_float),
        ("fVuPcsnDF_ms", c_float),
        ("fAccelNPcsnDF_ms", c_float),
        ("fAccelEPcsnDF_ms", c_float),
        ("fAccelUPcsnDF_ms", c_float),
        ("fTrackAngleDF_rad", c_float),
        ("fEntranceAngleDF_rad", c_float),
        ("fTargetAltDF_m", c_float),
        ("fMachDF_M", c_float),
        ("fTargetAzimAE_rad", c_float),
        ("fTargetPitchAE_rad", c_float),
        ("fTargetDistanceAE_m", c_float),
        ("fRadialVelocityAE_ms", c_float),
        ("fDisAlterRateAE_ms", c_float),
        ("fVnAE_ms", c_float),
        ("fVuAE_ms", c_float),
        ("fVeAE_ms", c_float),
        ("fTrackAngleAE_rad", c_float),
        ("fEnterAngleAE_rad", c_float),
        ("fAltAE_m", c_float),
        ("fMachAE_M", c_float),
        ("fTargetAzimIR_rad", c_float),
        ("fTargetPitchIR_rad", c_float),
        ("fTargetGrayIR", c_float),
        ("nTargetDisIR", c_int),
        ("nDisPreciseIR", c_int),
        ("fTargetDisIR_m", c_float),
        ("fVnIR_ms", c_float),
        ("fVuIR_ms", c_float),
        ("fVeIR_ms", c_float),
        ("fTrackAngleIR_rad", c_float),
        ("fEntranceAngleIR_rad", c_float),
        ("fMachIR_M", c_float),
        ("fDisAlterRateIR_ms", c_float),
        ("fTargetAzimEW_rad", c_float),
        ("fTargetPitchEW_rad", c_float),
        ("fTargetDisEW_m", c_float),
        ("fLastingTimeDL_s", c_float),
        ("nCampDL", c_int),
        ("nFormationTypeDL", c_int),
        ("nAltDL_m", c_int),
        ("fHeading_rad", c_float),
        ("fRadialVelocityDL_kmh", c_float),
        ("fVnDL_kmh", c_float),
        ("fVuDL_kmh", c_float),
        ("fVeDL_kmh", c_float),
        ("fLonDL_rad", c_float),
        ("fLatDL_rad", c_float),
        ("fNorthPosDL_m", c_float),
        ("fEastPosDL_m", c_float),
    ]


class CommonInfo(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("bMainWpnState", c_bool),
        ("bAssWpnState", c_bool),
        ("nAAMMissileNum", c_int),
        ("nSAAMMissileNum", c_int),
        ("fFuelInPlane_kg", c_float),
    ]


class FireControlRDM(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("fRaero_km", c_float),
        ("fRopt_km", c_float),
        ("fRpi_km", c_float),
        ("fRtr_km", c_float),
        ("fRacue_km", c_float),
        ("fRmin_km", c_float),
        ("fRmax_km", c_float),
        ("fAFPole_km", c_float),
        ("fDMC_deg", c_float),
        ("fOperatingDotAzim_rad", c_float),
        ("fOperatingDotPitch_rad", c_float),
        ("fOperatingCirleDiameter_rad", c_float),
        ("fClimAgl_deg", c_float),
        ("fPreLanuchTime_s", c_float),
        ("fMPI", c_float),
        ("nAttackIndication", c_int),
    ]


class FireControlIRM(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("fRmax_km", c_float),
        ("fRmin_km", c_float),
        ("fRtr_km", c_float),
        ("fSeekerAzim_rad", c_float),
        ("fSeekerPitch_rad", c_float),
        ("fSeekerAzimP_rad", c_float),
        ("fSeekerPitchP_rad", c_float),
        ("nAttackIndication", c_int),
        ("bIsTracked", c_bool),
        ("bIsOverMaxOffAxisAgl", c_bool),
    ]


class MslProperty(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("nLoseTimeValid", c_int),
        ("nAFPoleALValid", c_int),
        ("nType", c_int),
        ("nSeekerState", c_int),
        ("nTargetLot", c_int),
        ("fMslAzim_rad", c_float),
        ("fMslPitch_rad", c_float),
        ("fMslDis_km", c_float),
        ("fHitPercentage", c_float),
        ("fAssFlagAzim_rad", c_float),
        ("fAssFlagPitch_rad", c_float),
        ("fSeekerOpen", c_float),
        ("fLoseTime_s", c_float),
        ("fAFPoleAL_km", c_float),
    ]


class FCMInfo(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("nLot", c_int),
        ("fTargetMach_M", c_float),
        ("fTargetAlt_m", c_float),
        ("fTargetDis_km", c_float),
        ("fDisAlterRate_ms", c_float),
        ("fEnterAngle_rad", c_float),
        ("sFCMRDM", FireControlRDM),
        ("sFCMIRM", FireControlIRM),
        ("nMslPropertyNum", c_int),
        ("sMslProperty", MslProperty * 6),
    ]


class StateInfo(Structure):
    _fields_ = [
        ("nAvionicsMode", c_int),
        ("nAEPowerByDL", c_int),
        ("nRadiateManager", c_int),
        ("bICNIPower", c_bool),
        ("bJIDSPower", c_bool),
        ("bEWSPower", c_bool),
        ("bAEPower", c_bool),
        ("bOEDEPower", c_bool),
        ("nAEWorkMode", c_int),
        ("bAEIsRadiate", c_bool),
        ("bIsHPECM", c_bool),
        ("bIsFireHPECM", c_bool),
        ("nAEOPState", c_int),
        ("nAEACMMode", c_int),
        ("bAETargetAbort", c_bool),
        ("bAESTAS", c_bool),
        ("bAESTT", c_bool),
        ("nAEAADisMeasure", c_int),
        ("nAESphereSelect", c_int),
        ("nAETargetVelThreshold", c_int),
        ("bAEFakeGuideSignal", c_bool),
        ("nAEAAScanLines", c_int),
        ("nAEAAScanScale", c_int),
        ("fAEScanCenterAzim_rad", c_float),
        ("fAEScanCenterPitch_rad", c_float),
        ("nEWWorkMode", c_int),
        ("bIsCanRadiate", c_bool),
        ("bHPECMAsk", c_bool),
        ("bHighPresure", c_bool),
        ("bLaunchBait", c_bool),
        ("bWarnMslNearing", c_bool),
        ("bWarnMslLaunched", c_bool),
        ("nLeftFrontRadiation", c_int),
        ("nRightFrontRadiation", c_int),
        ("nBackRadiation", c_int),
        ("nPJammProSelect", c_int),
        ("bIsProCanSelect", c_bool * 7),
        ("bFlame", c_bool * 3),
        ("bIsLeftValid", c_bool),
        ("nBaitLeftState", c_int),
        ("nBaitLeftLaunchState", c_int),
        ("bIsRightValid", c_bool),
        ("nBaitRightState", c_int),
        ("nBaitRightLaunchState", c_int),
        ("nOEDEWorkState", c_int),
        ("nOETrackMethod", c_int),
        ("nOELaserState", c_int),
        ("nOETrackingState", c_int),
        ("bOELaserRadiate", c_bool),
        ("nOEAzimScanRange", c_int),
        ("nOEPitchScanRange", c_int),
        ("nMainWpnType", c_int),
        ("nTargetAlloc", c_int * 3),
        ("nAllyLot", c_int),
        ("nRCSType", c_int),
        ("nRCSType_Auto", c_int),
        ("nChaffLeftNum", c_int),
        ("nFlameLeftNum", c_int),
        ("bActiveBaitDropAdvise", c_bool),
    ]


class AIMInfoBack(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("nDLRecvFlag", c_int),
        ("bTrackingFlag", c_bool),
        ("bSeekerHPFlag", c_bool),
        ("bDataLineState", c_bool),
        ("fVx", c_float),
        ("fVy", c_float),
        ("fVz", c_float),
        ("fXe", c_float),
        ("fYe", c_float),
        ("fZe", c_float),
        ("fMTDistance", c_float),
    ]


class TargetInList(Structure):
    _fields_ = [
        ("bTargetWpnTypeMatchValid", c_bool),
        ("bTargetTypeValid", c_bool),
        ("bTargetModelValid", c_bool),
        ("bTrackProbabilityValid", c_bool),
        ("bMPIValid", c_bool),
        ("bTargetDisAlterRateValid", c_bool),
        ("bTargetDisValid", c_bool),
        ("bTargetLotValid", c_bool),
        ("bTargetPrecisionContent", c_bool),
        ("nEnvelopeType", c_int),
        ("bRaeroValid", c_bool),
        ("bPoptValid", c_bool),
        ("bRpiValid", c_bool),
        ("bRtrValid", c_bool),
        ("bRacueValid", c_bool),
        ("bRminValid", c_bool),
        ("bRmaxValid", c_bool),
        ("bFourAttackRegionValid", c_bool),
        ("nLot", c_int),
        ("nDisPre", c_int),
        ("nTargetDisBookbindAndExtrapolateAttr", c_int),
        ("nTargetAttackParameter", c_int),
        ("nTargetWpnTypeMatch", c_int),
        ("nPreciseType", c_int),
        ("nPlatformnIdentify", c_int),
        ("fTrackProbability", c_float),
        ("fMPI", c_float),
        ("fTheoryRaero_km", c_float),
        ("fRopt_km", c_float),
        ("fRpi_km", c_float),
        ("fRacue_km", c_float),
        ("fRtr_km", c_float),
        ("fRmin_km", c_float),
        ("fRmax_km", c_float),
        ("fDisAlterRate", c_float),
        ("fDis", c_float),
        ("nDLTargetLot", c_int),
    ]


class TacticalManagerInfo(Structure):
    _fields_ = [
        ("nTargetInListNum", c_int),
        ("sTargetInListData", TargetInList * 8),
    ]


class FighterPara(Structure):
    _fields_ = [
        ("fRealAzimuth_rad_rad", c_float),
        ("fMagneticAzimuth_rad", c_float),
        ("fGroundSpeed_ms", c_float),
        ("fDriftAngle_rad", c_float),
        ("fHorizontalTrackAngle_rad", c_float),
        ("fWindSpeed_ms", c_float),
        ("fWindDirection", c_float),
        ("dLongtitude_rad", c_double),
        ("dLatitude_rad", c_double),
        ("fAltitude_m", c_float),
        ("fHeading_rad", c_float),
        ("fPitch_rad", c_float),
        ("fRoll_rad", c_float),
        ("fVn_ms", c_float),
        ("fVu_ms", c_float),
        ("fVe_ms", c_float),
        ("fAccN_ms2", c_float),
        ("fAccU_ms2", c_float),
        ("fAccE_ms2", c_float),
        ("fAbsAlt_m", c_float),
        ("fRadioAlt_m", c_float),
        ("fRealAirspeed_kmh", c_float),
        ("fCalibratedAlt_m", c_float),
        ("fMach_M", c_float),
        ("fCAS_kmh", c_float),
        ("fNormalAcc_g", c_float),
        ("fVTrackAngle_rad", c_float),
        ("fMaxAttackAngle_rad", c_float),
        ("fMinAttackAngle_rad", c_float),
        ("fMaxCAS_kmh", c_float),
        ("fMinCAS_kmh", c_float),
        ("fMaxMach_M", c_float),
        ("fMaxNormalOverload_g", c_float),
        ("fMinNormalOverload_g", c_float),
    ]


class AlarmInfo(Structure):
    _fields_ = [
        ("bValid", c_bool),
        ("fMisAzi", c_float),
        ("fMisEle", c_float),
    ]


class otherInfo(Structure):
    _fields_ = [
        ("bOver", c_bool),
        ("nEndReason", c_int),
        ("fAggregateScore", c_float),
        ("fReward", c_float),
        ("nAlarmNum", c_int),
        ("sAlarm", AlarmInfo * 15),
    ]


class AIData(Structure):
    _fields_ = [
        ("AATargetDataListNum", c_int),
        ("sAATargetData", AATargetInfo * 20),
        ("sSMSData", CommonInfo),
        ("sFCMData", FCMInfo),
        ("sStateData", StateInfo),
        ("nAIMInfoInfoNum", c_int),
        ("sAIMInfo", AIMInfoBack * 6),
        ("sAttackList", TacticalManagerInfo),
        ("sFighterPara", FighterPara),
        ("sOtherInfo", otherInfo),
    ]


class decision_data(Structure):
    _fields_ = [
        ("stage", c_int),
        ("M_No_p", c_int),
        ("shoot_p", c_bool),
        ("LZ", c_int),
        ("Cindex", c_int),
        ("h_dive", c_float),
        ("h_climb", c_float),
        ("JS", c_int),
        ("time", c_float),
        ("iEvade", c_int),
        ("bLockOnNTS", c_bool),
        ("bAssignNTS", c_bool),
        ("sttTime", c_float),
        ("tasTime", c_float),
        ("tarLotNum", c_int),
        ("tarLot", c_int),
        ("pointNum", c_int),
        ("lastpointTime", c_float),
    ]


def iter_assign(target, src):
    fields = getattr(target, '_fields_', [])
    for fieldname, fmt in fields:
        if hasattr(src, fieldname):
            status = getattr(target, fieldname)
            if isinstance(status, Structure) or isinstance(status, Array):
                break
            value = getattr(src, fieldname)
            if math.isnan(value) or math.isinf(value):  # outlier detection
                value = 0
            setattr(target, fieldname, value)
        else:
            setattr(target, fieldname, 0)


def situation_to_old_situation(situation):
    rule_input = AIData()
    rule_input.AATargetDataListNum = situation.AATargetDataListNum
    for i in range(rule_input.AATargetDataListNum):
        iter_assign(rule_input.sAATargetData[i], situation.sAATargetData[i])
    iter_assign(rule_input.sSMSData, situation.sSMSData)
    iter_assign(rule_input.sFCMData, situation.sFCMData)
    iter_assign(rule_input.sFCMData.sFCMRDM, situation.sFCMData.sFCMRDM)
    iter_assign(rule_input.sFCMData.sFCMIRM, situation.sFCMData.sFCMIRM)
    rule_input.sFCMData.nMslPropertyNum = situation.sFCMData.nMslPropertyNum
    for i in range(rule_input.sFCMData.nMslPropertyNum):
        iter_assign(rule_input.sFCMData.sMslProperty[i], situation.sFCMData.sMslProperty[i])
    iter_assign(rule_input.sStateData, situation.sStateData)
    rule_input.nAIMInfoInfoNum = situation.nAIMInfoInfoNum
    for i in range(rule_input.nAIMInfoInfoNum):
        iter_assign(rule_input.sAIMInfo, situation.sAIMInfo)
    rule_input.sAttackList.nTargetInListNum = situation.sAttackList.nTargetInListNum
    for i in range(rule_input.sAttackList.nTargetInListNum):
        iter_assign(rule_input.sAttackList.sTargetInListData[i],
                    situation.sAttackList.sTargetInListData[i])
    iter_assign(rule_input.sFighterPara, situation.sFighterPara)
    iter_assign(rule_input.sOtherInfo, situation.sOtherInfo)
    if situation.sOtherInfo.nAlarmNum > 15:
        situation.sOtherInfo.nAlarmNum = 15
    rule_input.sOtherInfo.nAlarmNum = situation.sOtherInfo.nAlarmNum
    for i in range(rule_input.sOtherInfo.nAlarmNum):
        iter_assign(rule_input.sOtherInfo.sAlarm[i], situation.sOtherInfo.sAlarm[i])
    return rule_input


class PlaneSituationDecoder:

    def __init__(self):
        pass

    def v_xyz_to_speed(self, plane_situation):
        v_x = 300
        v_y = 0
        v_z = 0
        if len(plane_situation.aaTargetData) > 0:
            for i in plane_situation.aaTargetData:
                if i.bAETarget:
                    v_x = i.fVnDF_ms
                    v_y = i.fVuDF_ms
                    v_z = i.fVeDF_ms
                    break
                elif i.bDLTarget:
                    v_x = i.fVnDL_kmh / 3.6
                    v_y = i.fVuDL_kmh / 3.6
                    v_z = i.fVeDL_kmh / 3.6
        enemy_speed = (v_x**2 + v_y**2 + v_z**2)**0.5
        return enemy_speed

    def decode_AIAlgo(self, plane_situation):
        """
        @describe: decode interface data for AIAlgo
        @author: BUAA
        @return: decoded data
        """
        x = self.__get_distance(plane_situation.dLatitude_rad, plane_situation.dLongtitude_rad,
                                30.0 * math.pi / 180.0, plane_situation.dLongtitude_rad, True)
        y = self.__get_distance(plane_situation.dLatitude_rad, plane_situation.dLongtitude_rad,
                                plane_situation.dLatitude_rad, 115.0 * math.pi / 180.0, True)
        if plane_situation.dLongtitude_rad < 115.0 * math.pi / 180.0:
            # fix
            y = 0 - y
        if plane_situation.dLatitude_rad < 30.0 * math.pi / 180.0:
            # fix
            x = 0 - x
        situation_self = {
            'fPitchAngle':
                plane_situation.fPitch_rad / math.pi * 180.0,
            'fRollAngle':
                plane_situation.fRoll_rad / math.pi * 180.0,
            'fYawAngle':
                plane_situation.fHeading_rad / math.pi * 180.0,
            'fTrueAirSpeed':
                plane_situation.fRealAirspeed_kmh / 3.6,
            'fAltitude':
                plane_situation.fAltitude_m,
            'dLongitude':
                plane_situation.dLongtitude_rad / math.pi * 180.0,
            'dLatitude':
                plane_situation.dLatitude_rad / math.pi * 180.0,
            'fNormalLoad':
                plane_situation.fNormalAcc_g,
            'fMass':
                plane_situation.fFuelInPlane_kg,
            # TODO:速率值不正确
            # 'fRollRate': plane_situation.fRoll_rad,
            'fRollRate':
                0.0,
            'fAcceleration':
                math.sqrt(plane_situation.fAccN_ms2**2 + plane_situation.fAccU_ms2**2 +
                          plane_situation.fAccE_ms2**2),
            'x':
                x * 1000.0,
            'y':
                y * 1000.0
        }

        altitude_m = 0
        pitch_deg = 0
        yaw_deg = 0

        if len(plane_situation.aaTargetData) > 0:
            for target in plane_situation.aaTargetData:
                altitude_m = target.fTargetAltDF_m
                pitch_deg = math.atan(
                    target.fVuDF_ms /
                    math.sqrt(target.fVnDF_ms**2 + target.fVeDF_ms**2 + 0.00001)) / math.pi * 180.0
                yaw_deg = math.acos(
                    target.fVnDF_ms /
                    math.sqrt(target.fVnDF_ms**2 + target.fVeDF_ms**2 + 0.00001)) / math.pi * 180.0
                # print("DL:", target.fVeDL_kmh)
                # print("DF:", target.fVeDF_ms)
                if target.fVeDF_ms < 0:
                    yaw_deg = 0 - yaw_deg
                if target.bAETarget:
                    break

                    # print("DL:", target.fVeDL_kmh)
                    # print("DF:", target.fVeDF_ms)

            for i, target in enumerate(plane_situation.aaTargetData):
                if target.bDLTarget:
                    # fix
                    x = self.__get_distance(target.fLatDL_rad, target.fLonDL_rad,
                                            30.0 * math.pi / 180.0, target.fLonDL_rad, True)
                    y = self.__get_distance(target.fLatDL_rad, target.fLonDL_rad, target.fLatDL_rad,
                                            115.0 * math.pi / 180.0, True)
                    if target.fLonDL_rad < 115.0 * math.pi / 180.0:
                        y = 0 - y
                    if target.fLatDL_rad < 30.0 * math.pi / 180.0:
                        x = 0 - x
        # TODO:修复敌人速度
        enemy_speed = self.v_xyz_to_speed(plane_situation)
        # todo:end
        situation_enemy = {
            'fPitchAngle': pitch_deg,
            'fRollAngle': 0.0,
            'fYawAngle': yaw_deg,
            # 'fTrueAirSpeed': plane_situation.fRealAirspeed_kmh / 3.6,
            'fTrueAirSpeed': enemy_speed,
            'fAltitude': altitude_m,
            'dLongitude': plane_situation.dLongtitude_rad / math.pi * 180.0,
            'dLatitude': plane_situation.dLatitude_rad / math.pi * 180.0,
            'fNormalLoad': 1.0,
            'fMass': 0.0,
            'fRollRate': 0,
            'fAcceleration': 0,
            'x': x * 1000.0,
            'y': y * 1000.0
        }
        situation_self['fTrueAirSpeed'] = situation_enemy['fTrueAirSpeed']
        return situation_self, situation_enemy

    def __get_distance(self, lat1, lon1, lat2, lon2, bRad=False):
        """
        @describe: get distance between two geo point
        @author: BUAA
        :param lat1:
        :param lon1:
        :param lat2:
        :param lon2:
        :param bRad: if the unit is rad, then set it to True
        :return:
        """
        if not bRad:
            __lat1 = lat1 * math.pi / 180.0
            __lon1 = lon1 * math.pi / 180.0
            __lat2 = lat2 * math.pi / 180.0
            __lon2 = lon2 * math.pi / 180.0
        else:
            __lat1 = lat1
            __lon1 = lon1
            __lat2 = lat2
            __lon2 = lon2

        vLon = abs(__lon1 - __lon2)
        vLat = abs(__lat1 - __lat2)

        distance = 2 * math.asin(math.sqrt(
            (math.sin(vLat / 2) ** 2) + \
            (math.cos(__lat1) * math.cos(__lat2) * (math.sin(vLon / 2) ** 2))
        )) * 6371.7

        return distance

    def old_sitiuation_to_ptd_model(self, rule_input):
        input_value = PlaneSituationModel()
        input_value.nTargetDataListNum = rule_input.AATargetDataListNum

        input_value.aaTargetData = [PlaneSituationModelAATargetData()] * input_value.nTargetDataListNum
        for i in range(input_value.nTargetDataListNum):
            input_value.aaTargetData[i].bValid = rule_input.sAATargetData[i].bValid
            input_value.aaTargetData[i].nAllyLot = rule_input.sAATargetData[i].nAllyLot
            input_value.aaTargetData[i].nAELot = rule_input.sAATargetData[i].nAELot
            input_value.aaTargetData[i].nEWLot = rule_input.sAATargetData[i].nEWLot
            input_value.aaTargetData[i].nDLLot = rule_input.sAATargetData[i].nDLLot
            input_value.aaTargetData[i].bNTS = rule_input.sAATargetData[i].bNTS
            input_value.aaTargetData[i].nAESAWorkState = rule_input.sAATargetData[i].nAESAWorkState
            input_value.aaTargetData[i].bAETarget = rule_input.sAATargetData[i].bAETarget
            input_value.aaTargetData[i].bEWTarget = rule_input.sAATargetData[i].bEWTarget
            input_value.aaTargetData[i].bDLTarget = rule_input.sAATargetData[i].bDLTarget
            input_value.aaTargetData[i].nJamDegree = rule_input.sAATargetData[i].nJamDegree

            input_value.aaTargetData[i].nIdentifyResults = rule_input.sAATargetData[i].nIdentifyResults
            input_value.aaTargetData[i].nIdentifyAttackResults = rule_input.sAATargetData[i].nIdentifyAttackResults
            input_value.aaTargetData[i].fTargetDistanceDF_m = rule_input.sAATargetData[i].fTargetDistanceDF_m
            input_value.aaTargetData[i].fDisAlterRateDF_ms = rule_input.sAATargetData[i].fDisAlterRateDF_ms
            input_value.aaTargetData[i].fTargetAzimDF_rad = rule_input.sAATargetData[i].fTargetAzimDF_rad
            input_value.aaTargetData[i].fTargetPitchDF_rad = rule_input.sAATargetData[i].fTargetPitchDF_rad
            input_value.aaTargetData[i].fTargetAzimVelGDF_rads = rule_input.sAATargetData[i].fTargetAzimVelGDF_rads
            input_value.aaTargetData[i].fTargetPitchVelGDF_rads = rule_input.sAATargetData[i].fTargetPitchVelGDF_rads
            input_value.aaTargetData[i].fVnDF_ms = rule_input.sAATargetData[i].fVnDF_ms
            input_value.aaTargetData[i].fVuDF_ms = rule_input.sAATargetData[i].fVuDF_ms
            input_value.aaTargetData[i].fVeDF_ms = rule_input.sAATargetData[i].fVeDF_ms
            input_value.aaTargetData[i].fAccNDF_ms2 = rule_input.sAATargetData[i].fAccNDF_ms2
            input_value.aaTargetData[i].fAccUDF_ms2 = rule_input.sAATargetData[i].fAccUDF_ms2
            input_value.aaTargetData[i].fAccEDF_ms2 = rule_input.sAATargetData[i].fAccEDF_ms2
            input_value.aaTargetData[i].fDisPrecisionDF_m = rule_input.sAATargetData[i].fDisPrecisionDF_m
            input_value.aaTargetData[i].fDisRatePrecisionDF_ms = rule_input.sAATargetData[i].fDisRatePrecisionDF_ms
            input_value.aaTargetData[i].fAzimPrecisionBDF_mrad = rule_input.sAATargetData[i].fAzimPrecisionBDF_mrad
            input_value.aaTargetData[i].fPitchPrecisionDF_mrad = rule_input.sAATargetData[i].fPitchPrecisionDF_mrad
            input_value.aaTargetData[i].fEntranceAngleDF_rad = rule_input.sAATargetData[i].fEntranceAngleDF_rad
            input_value.aaTargetData[i].fTargetAltDF_m = rule_input.sAATargetData[i].fTargetAltDF_m
            input_value.aaTargetData[i].fMachDF_M = rule_input.sAATargetData[i].fMachDF_M
            input_value.aaTargetData[i].fTargetAzimAE_rad = rule_input.sAATargetData[i].fTargetAzimAE_rad
            input_value.aaTargetData[i].fTargetPitchAE_rad = rule_input.sAATargetData[i].fTargetPitchAE_rad
            input_value.aaTargetData[i].fTargetDistanceAE_m = rule_input.sAATargetData[i].fTargetDistanceAE_m
            input_value.aaTargetData[i].fRadialVelocityAE_ms = rule_input.sAATargetData[i].fRadialVelocityAE_ms
            input_value.aaTargetData[i].fDisAlterRateAE_ms = rule_input.sAATargetData[i].fDisAlterRateAE_ms
            input_value.aaTargetData[i].fVnAE_ms = rule_input.sAATargetData[i].fVnAE_ms
            input_value.aaTargetData[i].fVuAE_ms = rule_input.sAATargetData[i].fVuAE_ms
            input_value.aaTargetData[i].fVeAE_ms = rule_input.sAATargetData[i].fVeAE_ms
            input_value.aaTargetData[i].fEnterAngleAE_rad = rule_input.sAATargetData[i].fEnterAngleAE_rad
            input_value.aaTargetData[i].fAltAE_m = rule_input.sAATargetData[i].fAltAE_m
            input_value.aaTargetData[i].fMachAE_M = rule_input.sAATargetData[i].fMachAE_M
            input_value.aaTargetData[i].fTargetAzimEW_rad = rule_input.sAATargetData[i].fTargetAzimEW_rad
            input_value.aaTargetData[i].fTargetPitchEW_rad = rule_input.sAATargetData[i].fTargetPitchEW_rad
            input_value.aaTargetData[i].fLastingTimeDL_s = rule_input.sAATargetData[i].fLastingTimeDL_s
            input_value.aaTargetData[i].nAltDL_m = rule_input.sAATargetData[i].nAltDL_m
            input_value.aaTargetData[i].fHeading_rad = rule_input.sAATargetData[i].fHeading_rad
            input_value.aaTargetData[i].fRadialVelocityDL_kmh = rule_input.sAATargetData[i].fRadialVelocityDL_kmh
            input_value.aaTargetData[i].fVnDL_kmh = rule_input.sAATargetData[i].fVnDL_kmh
            input_value.aaTargetData[i].fVuDL_kmh = rule_input.sAATargetData[i].fVuDL_kmh
            input_value.aaTargetData[i].fVeDL_kmh = rule_input.sAATargetData[i].fVeDL_kmh
            input_value.aaTargetData[i].fLonDL_rad = rule_input.sAATargetData[i].fLonDL_rad
            input_value.aaTargetData[i].fLatDL_rad = rule_input.sAATargetData[i].fLatDL_rad
            input_value.aaTargetData[i].fNorthPosDL_m = rule_input.sAATargetData[i].fNorthPosDL_m
            input_value.aaTargetData[i].fEastPosDL_m = rule_input.sAATargetData[i].fEastPosDL_m
            
        input_value.SMSInfo_bValid = rule_input.sSMSData.bValid
        input_value.bMainWpnState = rule_input.sSMSData.bMainWpnState
        input_value.nAAMMissileNum = rule_input.sSMSData.nAAMMissileNum
        input_value.fFuelInPlane_kg = rule_input.sSMSData.fFuelInPlane_kg

        input_value.FCMInfo_bValid = rule_input.sFCMData.bValid
        input_value.nLot = rule_input.sFCMData.nLot
        input_value.fTargetMach_M = rule_input.sFCMData.fTargetMach_M
        input_value.fTargetAlt_m = rule_input.sFCMData.fTargetAlt_m
        input_value.fTargetDis_km = rule_input.sFCMData.fTargetDis_km
        input_value.fDisAlterRate_ms = rule_input.sFCMData.fDisAlterRate_ms
        input_value.fEnterAngle_rad = rule_input.sFCMData.fEnterAngle_rad
        input_value.sFCMRDM_bValid = rule_input.sFCMData.sFCMRDM.bValid
        input_value.fRaero_km = rule_input.sFCMData.sFCMRDM.fRaero_km
        input_value.fRopt_km = rule_input.sFCMData.sFCMRDM.fRopt_km
        input_value.fRpi_km = rule_input.sFCMData.sFCMRDM.fRpi_km
        input_value.sFCMRDM_fRtr_km = rule_input.sFCMData.sFCMRDM.fRtr_km
        input_value.fRacue_km = rule_input.sFCMData.sFCMRDM.fRacue_km
        input_value.sFCMRDM_fRmin_km = rule_input.sFCMData.sFCMRDM.fRmin_km
        input_value.sFCMRDM_fRmax_km = rule_input.sFCMData.sFCMRDM.fRmax_km
        input_value.nAttackIndication = rule_input.sFCMData.sFCMRDM.nAttackIndication
        input_value.nMslPropertyNum = rule_input.sFCMData.nMslPropertyNum

        input_value.nRadiateManager = rule_input.sStateData.nRadiateManager
        input_value.bJIDSPower = rule_input.sStateData.bJIDSPower
        input_value.bAEIsRadiate = rule_input.sStateData.bAEIsRadiate
        input_value.nAEOPState = rule_input.sStateData.nAEOPState
        input_value.bAESTAS = rule_input.sStateData.bAESTAS
        input_value.bAESTT = rule_input.sStateData.bAESTT
        input_value.nAEAADisMeasure = rule_input.sStateData.nAEAADisMeasure
        input_value.nAEAAScanLines = rule_input.sStateData.nAEAAScanLines
        input_value.nAEAAScanScale = rule_input.sStateData.nAEAAScanScale
        input_value.fAEScanCenterAzim_rad = rule_input.sStateData.fAEScanCenterAzim_rad
        input_value.fAEScanCenterPitch_rad = rule_input.sStateData.fAEScanCenterPitch_rad
        input_value.bWarnMslNearing = rule_input.sStateData.bWarnMslNearing
        input_value.bWarnMslLaunched = rule_input.sStateData.bWarnMslLaunched
        input_value.nRCSType = rule_input.sStateData.nRCSType
        input_value.nRCSType_Auto = rule_input.sStateData.nRCSType_Auto
        input_value.nChaffLeftNum = rule_input.sStateData.nChaffLeftNum

        input_value.nAIMInfoInfoNum = rule_input.nAIMInfoInfoNum
        input_value.sAIMInfo = [PlaneSituationModelAIMInfoBack()] * input_value.nAIMInfoInfoNum
        for i in range(input_value.nAIMInfoInfoNum):
            input_value.sAIMInfo[i].PL15_bValid = rule_input.sAIMInfo[i].bValid
            input_value.sAIMInfo[i].bTrackingFlag = rule_input.sAIMInfo[i].bTrackingFlag
            input_value.sAIMInfo[i].bSeekerHPFlag = rule_input.sAIMInfo[i].bSeekerHPFlag
            input_value.sAIMInfo[i].fVx = rule_input.sAIMInfo[i].fVx
            input_value.sAIMInfo[i].fVy = rule_input.sAIMInfo[i].fVy
            input_value.sAIMInfo[i].fVz = rule_input.sAIMInfo[i].fVz
            input_value.sAIMInfo[i].fXe = rule_input.sAIMInfo[i].fXe
            input_value.sAIMInfo[i].fYe = rule_input.sAIMInfo[i].fYe
            input_value.sAIMInfo[i].fZe = rule_input.sAIMInfo[i].fZe
            input_value.sAIMInfo[i].fMTDistance = rule_input.sAIMInfo[i].fMTDistance

        input_value.nTargetInListNum = rule_input.sAttackList.nTargetInListNum
        input_value.sTargetInListData = [TargetInListData()] * input_value.nTargetInListNum
        for i in range(input_value.nTargetInListNum):
            input_value.sTargetInListData[i].nLot = rule_input.sAttackList.sTargetInListData[i].nLot
            input_value.sTargetInListData[i].nTargetAttackParameter = rule_input.sAttackList.sTargetInListData[i].nTargetAttackParameter
            input_value.sTargetInListData[i].fTheoryRaero_km = rule_input.sAttackList.sTargetInListData[i].fTheoryRaero_km
            input_value.sTargetInListData[i].fTheoryRopt_km = rule_input.sAttackList.sTargetInListData[i].fRopt_km
            input_value.sTargetInListData[i].fTheoryRpi_km = rule_input.sAttackList.sTargetInListData[i].fRpi_km
            input_value.sTargetInListData[i].fTheoryRacue_km = rule_input.sAttackList.sTargetInListData[i].fRacue_km
            input_value.sTargetInListData[i].fTheoryRtr_km = rule_input.sAttackList.sTargetInListData[i].fRtr_km
            input_value.sTargetInListData[i].fTheoryRmin_km = rule_input.sAttackList.sTargetInListData[i].fRmin_km
            input_value.sTargetInListData[i].fTheoryRmax_km = rule_input.sAttackList.sTargetInListData[i].fRmax_km
            input_value.sTargetInListData[i].fDisAlterRate = rule_input.sAttackList.sTargetInListData[i].fDisAlterRate
            input_value.sTargetInListData[i].fDis = rule_input.sAttackList.sTargetInListData[i].fDis

        input_value.dLongtitude_rad = rule_input.sFighterPara.dLongtitude_rad
        input_value.dLatitude_rad = rule_input.sFighterPara.dLatitude_rad
        input_value.fAltitude_m = rule_input.sFighterPara.fAltitude_m
        input_value.fHeading_rad = rule_input.sFighterPara.fHeading_rad
        input_value.fPitch_rad = rule_input.sFighterPara.fPitch_rad
        input_value.fRoll_rad = rule_input.sFighterPara.fRoll_rad
        input_value.fVn_ms = rule_input.sFighterPara.fVn_ms
        input_value.fVu_ms = rule_input.sFighterPara.fVu_ms
        input_value.fVe_ms = rule_input.sFighterPara.fVe_ms
        input_value.fAccN_ms2 = rule_input.sFighterPara.fAccN_ms2
        input_value.fAccU_ms2 = rule_input.sFighterPara.fAccU_ms2
        input_value.fAccE_ms2 = rule_input.sFighterPara.fAccE_ms2
        input_value.fAbsAlt_m = rule_input.sFighterPara.fAbsAlt_m
        input_value.fRadioAlt_m = rule_input.sFighterPara.fRadioAlt_m
        input_value.fRealAirspeed_kmh = rule_input.sFighterPara.fRealAirspeed_kmh
        input_value.fMach_M = rule_input.sFighterPara.fMach_M
        input_value.fNormalAcc_g = rule_input.sFighterPara.fNormalAcc_g
        input_value.fVTrackAngle_rad = rule_input.sFighterPara.fVTrackAngle_rad

        input_value.nAlarmNum = rule_input.sOtherInfo.nAlarmNum
        input_value.sMisAlarm = [AlarmInfo()] * input_value.nAlarmNum
        for i in range(input_value.nAlarmNum):
            input_value.sMisAlarm[i].MisAlarm_bValid = rule_input.sOtherInfo.sAlarm[i].bValid
            input_value.sMisAlarm[i].fMisAzi = rule_input.sOtherInfo.sAlarm[i].fMisAzi
            input_value.sMisAlarm[i].fMisEle = rule_input.sOtherInfo.sAlarm[i].fMisEle
        return input_value
