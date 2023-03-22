#!/usr/bin/env python3
""" Parent class for plane simtuation return data structure"""
""" AI <<<< simtuation """
from angrybirds.lib.structure import Structure


class AATargetInfo(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('i', 'nAllyLot'),
        ('i', 'nAELot'),
        ('i', 'nOELot'),
        ('i', 'nEWLot'),
        ('i', 'nDLLot'),
        ('i', 'nPlatformnIdentify'),
        ('?', 'bNTS'),
        ('i', 'nPrecisionType'),
        ('i', 'nIdentification'),
        ('i', 'nOESAWorkState'),
        ('i', 'nAESAWorkState'),
        ('?', 'bAETarget'),
        ('?', 'bOETarget'),
        ('?', 'bEWTarget'),
        ('?', 'bDLTarget'),
        ('i', 'nJamDegree'),
        ('i', 'nIdentify'),
        ('i', 'nIdentifyResults'),
        ('i', 'nIdentifyAttackResults'),
        ('i', 'nFormationTypes'),
        ('f', 'fTargetDistanceDF_m'),
        ('f', 'fDisAlterRateDF_ms'),
        ('f', 'fTargetAzimDF_rad'),
        ('f', 'fTargetPitchDF_rad'),
        ('f', 'fTargetAzimVelGDF_rads'),
        ('f', 'fTargetPitchVelGDF_rads'),
        ('f', 'fVnDF_ms'),
        ('f', 'fVuDF_ms'),
        ('f', 'fVeDF_ms'),
        ('f', 'fAccNDF_ms2'),
        ('f', 'fAccUDF_ms2'),
        ('f', 'fAccEDF_ms2'),
        ('f', 'fDisPrecisionDF_m'),
        ('f', 'fDisRatePrecisionDF_ms'),
        ('f', 'fAzimPrecisionBDF_mrad'),
        ('f', 'fPitchPrecisionDF_mrad'),
        ('f', 'fAzhimRatePcsnBDF_mrads'),
        ('f', 'fPitchRatePcsnBDF_mrads'),
        ('f', 'fVnPcsnDF_ms'),
        ('f', 'fVePcsnDF_ms'),
        ('f', 'fVuPcsnDF_ms'),
        ('f', 'fAccelNPcsnDF_ms'),
        ('f', 'fAccelEPcsnDF_ms'),
        ('f', 'fAccelUPcsnDF_ms'),
        ('f', 'fTrackAngleDF_rad'),
        ('f', 'fEntranceAngleDF_rad'),
        ('f', 'fTargetAltDF_m'),
        ('f', 'fMachDF_M'),
        ('f', 'fTargetAzimAE_rad'),
        ('f', 'fTargetPitchAE_rad'),
        ('f', 'fTargetDistanceAE_m'),
        ('f', 'fRadialVelocityAE_ms'),
        ('f', 'fDisAlterRateAE_ms'),
        ('f', 'fVnAE_ms'),
        ('f', 'fVuAE_ms'),
        ('f', 'fVeAE_ms'),
        ('f', 'fTrackAngleAE_rad'),
        ('f', 'fEnterAngleAE_rad'),
        ('f', 'fAltAE_m'),
        ('f', 'fMachAE_M'),
        ('f', 'fTargetAzimIR_rad'),
        ('f', 'fTargetPitchIR_rad'),
        ('f', 'fTargetGrayIR'),
        ('i', 'nTargetDisIR'),
        ('i', 'nDisPreciseIR'),
        ('f', 'fTargetDisIR_m'),
        ('f', 'fVnIR_ms'),
        ('f', 'fVuIR_ms'),
        ('f', 'fVeIR_ms'),
        ('f', 'fTrackAngleIR_rad'),
        ('f', 'fEntranceAngleIR_rad'),
        ('f', 'fMachIR_M'),
        ('f', 'fDisAlterRateIR_ms'),
        ('f', 'fTargetAzimEW_rad'),
        ('f', 'fTargetPitchEW_rad'),
        ('f', 'fTargetDisEW_m'),
        ('f', 'fLastingTimeDL_s'),
        ('i', 'nCampDL'),
        ('i', 'nFormationTypeDL'),
        ('i', 'nAltDL_m'),
        ('f', 'fHeading_rad'),
        ('f', 'fRadialVelocityDL_kmh'),
        ('f', 'fVnDL_kmh'),
        ('f', 'fVuDL_kmh'),
        ('f', 'fVeDL_kmh'),
        ('f', 'fLonDL_rad'),
        ('f', 'fLatDL_rad'),
        ('f', 'fNorthPosDL_m'),
        ('f', 'fEastPosDL_m'),
    ]


class CommonInfo(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('?', 'bMainWpnState'),
        ('?', 'bAssWpnState'),
        ('i', 'nAAMMissileNum'),
        ('i', 'nSAAMMissileNum'),
        ('f', 'fFuelInPlane_kg'),
    ]


class FireControlRDM(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('f', 'fRaero_km'),
        ('f', 'fRopt_km'),
        ('f', 'fRpi_km'),
        ('f', 'fRtr_km'),
        ('f', 'fRacue_km'),
        ('f', 'fRmin_km'),
        ('f', 'fRmax_km'),
        ('f', 'fAFPole_km'),
        ('f', 'fDMC_deg'),
        ('f', 'fOperatingDotAzim_rad'),
        ('f', 'fOperatingDotPitch_rad'),
        ('f', 'fOperatingCirleDiameter_rad'),
        ('f', 'fClimAgl_deg'),
        ('f', 'fPreLanuchTime_s'),
        ('f', 'fMPI'),
        ('i', 'nAttackIndication'),
    ]


class FireControlIRM(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('f', 'fRmax_km'),
        ('f', 'fRmin_km'),
        ('f', 'fRtr_km'),
        ('f', 'fSeekerAzim_rad'),
        ('f', 'fSeekerPitch_rad'),
        ('f', 'fSeekerAzimP_rad'),
        ('f', 'fSeekerPitchP_rad'),
        ('i', 'nAttackIndication'),
        ('?', 'bIsTracked'),
        ('?', 'bIsOverMaxOffAxisAgl'),
    ]


class MslProperty(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('i', 'nWeaponLot'),
        ('i', 'nLoseTimeValid'),
        ('i', 'nAFPoleALValid'),
        ('i', 'nType'),
        ('i', 'nSeekerState'),
        ('i', 'nTargetLot'),
        ('f', 'fMslAzim_rad'),
        ('f', 'fMslPitch_rad'),
        ('f', 'fMslDis_km'),
        ('f', 'fHitPercentage'),
        ('f', 'fAssFlagAzim_rad'),
        ('f', 'fAssFlagPitch_rad'),
        ('f', 'fSeekerOpen'),
        ('f', 'fLoseTime_s'),
        ('f', 'fAFPoleAL_km'),
    ]


class FCMInfo(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('i', 'nLot'),
        ('f', 'fTargetMach_M'),
        ('f', 'fTargetAlt_m'),
        ('f', 'fTargetDis_km'),
        ('f', 'fDisAlterRate_ms'),
        ('f', 'fEnterAngle_rad'),
        (FireControlRDM, 'sFCMRDM'),
        (FireControlIRM, 'sFCMIRM'),
    ]


class StateInfo(Structure):
    _fields_ = [
        ('i', 'nAvionicsMode'),
        ('i', 'nAEPowerByDL'),
        ('i', 'nRadiateManager'),
        ('?', 'bICNIPower'),
        ('?', 'bJIDSPower'),
        ('?', 'bEWSPower'),
        ('?', 'bAEPower'),
        ('?', 'bOEDEPower'),
        ('i', 'nAEWorkMode'),
        ('?', 'bAEIsRadiate'),
        ('?', 'bIsHPECM'),
        ('?', 'bIsFireHPECM'),
        ('i', 'nAEOPState'),
        ('i', 'nAEACMMode'),
        ('?', 'bAETargetAbort'),
        ('?', 'bAESTAS'),
        ('?', 'bAESTT'),
        ('i', 'nAEAADisMeasure'),
        ('i', 'nAESphereSelect'),
        ('i', 'nAETargetVelThreshold'),
        ('?', 'bAEFakeGuideSignal'),
        ('i', 'nAEAAScanLines'),
        ('i', 'nAEAAScanScale'),
        ('f', 'fAEScanCenterAzim_rad'),
        ('f', 'fAEScanCenterPitch_rad'),
        ('i', 'nEWWorkMode'),
        ('?', 'bIsCanRadiate'),
        ('?', 'bHPECMAsk'),
        ('?', 'bHighPresure'),
        ('?', 'bLaunchBait'),
        ('?', 'bWarnMslNearing'),
        ('?', 'bWarnMslLaunched'),
        ('i', 'nLeftFrontRadiation'),
        ('i', 'nRightFrontRadiation'),
        ('i', 'nBackRadiation'),
        ('i', 'nPJammProSelect'),
        ('?', 'bIsProCanSelect_0'),
        ('?', 'bIsProCanSelect_1'),
        ('?', 'bIsProCanSelect_2'),
        ('?', 'bIsProCanSelect_3'),
        ('?', 'bIsProCanSelect_4'),
        ('?', 'bIsProCanSelect_5'),
        ('?', 'bIsProCanSelect_6'),
        ('?', 'bFlame_0'),
        ('?', 'bFlame_1'),
        ('?', 'bFlame_2'),
        ('?', 'bIsLeftValid'),
        ('i', 'nBaitLeftState'),
        ('i', 'nBaitLeftLaunchState'),
        ('?', 'bIsRightValid'),
        ('i', 'nBaitRightState'),
        ('i', 'nBaitRightLaunchState'),
        ('i', 'nOEDEWorkState'),
        ('i', 'nOETrackMethod'),
        ('i', 'nOELaserState'),
        ('i', 'nOETrackingState'),
        ('?', 'bOELaserRadiate'),
        ('i', 'nOEAzimScanRange'),
        ('i', 'nOEPitchScanRange'),
        ('i', 'nMainWpnType'),
        ('i', 'nTargetAlloc_0'),
        ('i', 'nTargetAlloc_1'),
        ('i', 'nTargetAlloc_2'),
        ('i', 'nAllyLot'),
        ('i', 'nRCSType'),
        ('i', 'nRCSType_Auto'),
        ('i', 'nChaffLeftNum'),
        ('i', 'nFlameLeftNum'),
        ('?', 'bActiveBaitDropAdvise'),
    ]


class AIMInfoBack(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('i', 'nDLRecvFlag'),
        ('?', 'bTrackingFlag'),
        ('?', 'bSeekerHPFlag'),
        ('?', 'bDataLineState'),
        ('i', 'nWeaponLot'),
        ('f', 'fVx'),
        ('f', 'fVy'),
        ('f', 'fVz'),
        ('f', 'fXe'),
        ('f', 'fYe'),
        ('f', 'fZe'),
        ('f', 'fMTDistance'),
    ]


class TargetInList(Structure):
    _fields_ = [
        ('?', 'bTargetWpnTypeMatchValid'),
        ('?', 'bTargetTypeValid'),
        ('?', 'bTargetModelValid'),
        ('?', 'bTrackProbabilityValid'),
        ('?', 'bMPIValid'),
        ('?', 'bTargetDisAlterRateValid'),
        ('?', 'bTargetDisValid'),
        ('?', 'bTargetLotValid'),
        ('?', 'bTargetPrecisionContent'),
        ('i', 'nEnvelopeType'),
        ('?', 'bRaeroValid'),
        ('?', 'bPoptValid'),
        ('?', 'bRpiValid'),
        ('?', 'bRtrValid'),
        ('?', 'bRacueValid'),
        ('?', 'bRminValid'),
        ('?', 'bRmaxValid'),
        ('?', 'bFourAttackRegionValid'),
        ('i', 'nLot'),
        ('i', 'nDisPre'),
        ('i', 'nTargetDisBookbindAndExtrapolateAttr'),
        ('i', 'nTargetAttackParameter'),
        ('i', 'nTargetWpnTypeMatch'),
        ('i', 'nPreciseType'),
        ('i', 'nPlatformnIdentify'),
        ('f', 'fTrackProbability'),
        ('f', 'fMPI'),
        ('f', 'fTheoryRaero_km'),
        ('f', 'fRopt_km'),
        ('f', 'fRpi_km'),
        ('f', 'fRacue_km'),
        ('f', 'fRtr_km'),
        ('f', 'fRmin_km'),
        ('f', 'fRmax_km'),
        ('f', 'fDisAlterRate'),
        ('f', 'fDis'),
        ('i', 'nDLTargetLot'),
    ]


class TacticalManagerInfo(Structure):
    _fields_ = [
        # ('i', 'nTargetInListNum'),  # random length
        # (TargetInList, 'sTargetInListData'),
    ]


class FighterPara(Structure):
    _fields_ = [
        ('f', 'fRealAzimuth_rad_rad'),
        ('f', 'fMagneticAzimuth_rad'),
        ('f', 'fGroundSpeed_ms'),
        ('f', 'fDriftAngle_rad'),
        ('f', 'fHorizontalTrackAngle_rad'),
        ('f', 'fWindSpeed_ms'),
        ('f', 'fWindDirection'),
        ('d', 'dLongtitude_rad'),
        ('d', 'dLatitude_rad'),
        ('f', 'fAltitude_m'),
        ('f', 'fHeading_rad'),
        ('f', 'fPitch_rad'),
        ('f', 'fRoll_rad'),
        ('f', 'fVn_ms'),
        ('f', 'fVu_ms'),
        ('f', 'fVe_ms'),
        ('f', 'fAccN_ms2'),
        ('f', 'fAccU_ms2'),
        ('f', 'fAccE_ms2'),
        ('f', 'fAbsAlt_m'),
        ('f', 'fRadioAlt_m'),
        ('f', 'fRealAirspeed_kmh'),
        ('f', 'fCalibratedAlt_m'),
        ('f', 'fMach_M'),
        ('f', 'fCAS_kmh'),
        ('f', 'fNormalAcc_g'),
        ('f', 'fVTrackAngle_rad'),
        ('f', 'fMaxAttackAngle_rad'),
        ('f', 'fMinAttackAngle_rad'),
        ('f', 'fMaxCAS_kmh'),
        ('f', 'fMinCAS_kmh'),
        ('f', 'fMaxMach_M'),
        ('f', 'fMaxNormalOverload_g'),
        ('f', 'fMinNormalOverload_g'),
    ]


class AlarmInfo(Structure):
    _fields_ = [
        ('?', 'bValid'),
        ('i', 'nTargetType'),
        ('i', 'nLot'),
        ('i', 'nEWLot'),
        ('?', 'bEWAdvise1'),
        ('?', 'bEWAdvise2'),
        ('?', 'bEWAdvise3'),
        ('?', 'bEWAdvise4'),
        ('?', 'bJamState1'),
        ('?', 'bJamState2'),
        ('?', 'bJamState3'),
        ('?', 'bJamState4'),
        ('f', 'fTargetRaero'),
        ('f', 'fTargetRtr'),
        ('i', 'nTargetEnvelopeType'),
        ('i', 'nIdentify'),
        ('i', 'nPlatformType'),
        ('i', 'nWeaponType'),
        ('?', 'bWarnMslNearing'),
        ('?', 'bWarnMslLaunched'),
        ('i', 'nIdentifyResults'),
        ('f', 'fDis'),
        ('f', 'fMisAzi'),
    ]


class otherInfo(Structure):
    _fields_ = [
        ('?', 'bOver'),
        ('i', 'nEndReason'),
        ('i', 'fAggregateScore'),
        ('i', 'fReward'),
    ]


class otherInfoSub(Structure):
    _fields_ = [
        ('i', 'nHitFighterWeaponLot'),
        ('i', 'nHitTargetWeaponLot'),
        ('d', 'dTimeStamp'),
        ('h', 'iCmdIndex'),
        ('H', 'iCmdID'),
    ]


class AIData(Structure):
    _fields_ = [
        ('<i', 'AATargetDataListNum'),  # random length
        (AATargetInfo, 'sAATargetData'),
        (CommonInfo, 'sSMSData'),
        (FCMInfo, 'sFCMData'),
        ('i', 'nMslPropertyNum'),  # random length
        (MslProperty, 'sMslProperty'),
        (StateInfo, 'sStateData'),
        ('i', 'nAIMInfoInfoNum'),  # random length
        (AIMInfoBack, 'sAIMInfo'),
        ('i', 'nTargetInListNum'),  # random length
        (TargetInList, 'sTargetInListData'),
        # (TacticalManagerInfo, 'sAttackList'),
        (FighterPara, 'sFighterPara'),
        (otherInfo, 'sOtherInfo'),
        ('i', 'nAlarmNum'),  # random length
        (AlarmInfo, 'sAlarm'),
        (otherInfoSub, 'stherInfoSub'),
    ]
    _ranges_ = {
        'AATargetDataListNum': (0, 20),
        'nMslPropertyNum': (0, 6),
        'nAIMInfoInfoNum': (0, 6),
        'nTargetInListNum': (0, 6),
        'nAlarmNum': (0, 10),
    }
