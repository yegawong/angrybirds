class PlaneSituationModelAATargetData:
    def __init__(self):
        self.bValid = 0
        self.nAllyLot = 0
        self.nAELot = 0
        self.nOELot = 0
        self.nEWLot = 0
        self.nDLLot = 0
        self.nPlatformnIdentify = 0
        self.bNTS = 0
        self.nPrecisionType = 0
        self.nIdentification = 0
        self.nOESAWorkState = 0
        self.nAESAWorkState = 0
        self.bAETarget = 0
        self.bOETarget = 0
        self.bEWTarget = 0
        self.bDLTarget = 0
        self.nJamDegree = 0
        self.nIdentify = 0
        self.nIdentifyResults = 0
        self.nIdentifyAttackResults = 0
        self.nFormationTypes = 0
        self.fTargetDistanceDF_m = 0
        self.fDisAlterRateDF_ms = 0
        self.fTargetAzimDF_rad = 0
        self.fTargetPitchDF_rad = 0
        self.fTargetAzimVelGDF_rads = 0
        self.fTargetPitchVelGDF_rads = 0
        self.fVnDF_ms = 0
        self.fVuDF_ms = 0
        self.fVeDF_ms = 0
        self.fAccNDF_ms2 = 0
        self.fAccUDF_ms2 = 0
        self.fAccEDF_ms2 = 0
        self.fDisPrecisionDF_m = 0
        self.fDisRatePrecisionDF_ms = 0
        self.fAzimPrecisionBDF_mrad = 0
        self.fPitchPrecisionDF_mrad = 0
        self.fAzhimRatePcsnBDF_mrads = 0
        self.fPitchRatePcsnBDF_mrads = 0
        self.fVnPcsnDF_ms = 0
        self.fVePcsnDF_ms = 0
        self.fVuPcsnDF_ms = 0
        self.fAccelNPcsnDF_ms = 0
        self.fAccelEPcsnDF_ms = 0
        self.fAccelUPcsnDF_ms = 0
        self.fTrackAngleDF_rad = 0
        self.fEntranceAngleDF_rad = 0
        self.fTargetAltDF_m = 0
        self.fMachDF_M = 0
        self.fTargetAzimAE_rad = 0
        self.fTargetPitchAE_rad = 0
        self.fTargetDistanceAE_m = 0
        self.fRadialVelocityAE_ms = 0
        self.fDisAlterRateAE_ms = 0
        self.fVnAE_ms = 0
        self.fVuAE_ms = 0
        self.fVeAE_ms = 0
        self.fTrackAngleAE_rad = 0
        self.fEnterAngleAE_rad = 0
        self.fAltAE_m = 0
        self.fMachAE_M = 0
        self.fTargetAzimIR_rad = 0
        self.fTargetPitchIR_rad = 0
        self.fTargetGrayIR = 0
        self.nTargetDisIR = 0
        self.nDisPreciseIR = 0
        self.fTargetDisIR_m = 0
        self.fVnIR_ms = 0
        self.fVuIR_ms = 0
        self.fVeIR_ms = 0
        self.fTrackAngleIR_rad = 0
        self.fEntranceAngleIR_rad = 0
        self.fMachIR_M = 0
        self.fDisAlterRateIR_ms = 0
        self.fTargetAzimEW_rad = 0
        self.fTargetPitchEW_rad = 0
        self.fTargetDisEW_m = 0
        self.fLastingTimeDL_s = 0
        self.nCampDL = 0
        self.nFormationTypeDL = 0
        self.nAltDL_m = 0
        self.fHeading_rad = 0
        self.fRadialVelocityDL_kmh = 0
        self.fVnDL_kmh = 0
        self.fVuDL_kmh = 0
        self.fVeDL_kmh = 0
        self.fLonDL_rad = 0
        self.fLatDL_rad = 0
        self.fNorthPosDL_m = 0
        self.fEastPosDL_m = 0


class PlaneSituationModelMslProperty:
    def __init__(self):
        self.MslPro_bValid = 0
        self.MslPro_nLot = 0
        self.nLoseTimeValid = 0
        self.nAFPoleALValid = 0
        self.nType = 0
        self.nSeekerState = 0
        self.nTargetLot = 0
        self.fMslAzim_rad = 0
        self.fMslPitch_rad = 0
        self.fMslDis_km = 0
        self.fHitPercentage = 0
        self.fAssFlagAzim_rad = 0
        self.fAssFlagPitch_rad = 0
        self.fSeekerOpen = 0
        self.fLoseTime_s = 0
        self.fAFPoleAL_km = 0


class TargetInListData:
    def __init__(self):
        self.bTargetWpnTypeMatchValid = 0
        self.bTargetTypeValid = 0
        self.bTargetModelValid = 0
        self.bTrackProbabilityValid = 0
        self.bMPIValid = 0
        self.bTargetDisAlterRateValid = 0
        self.bTargetDisValid = 0
        self.bTargetLotValid = 0
        self.bTargetPrecisionContent = 0
        self.nEnvelopeType = 0
        self.bRaeroValid = 0
        self.bPoptValid = 0
        self.bRpiValid = 0
        self.bRtrValid = 0
        self.bRacueValid = 0
        self.bRminValid = 0
        self.bRmaxValid = 0
        self.bFourAttackRegionValid = 0
        self.nLot = 0
        self.nDisPre = 0
        self.nTargetDisBookbindAndExtrapolateAttr = 0
        self.nTargetAttackParameter = 0
        self.nTargetWpnTypeMatch = 0
        self.nPreciseType = 0
        self.nTargetInListData_PlatformnIdentify = 0
        self.fTrackProbability = 0
        self.fMPI = 0
        self.fTheoryRaero_km = 0
        self.fTheoryRopt_km = 0
        self.fTheoryRpi_km = 0
        self.fTheoryRacue_km = 0
        self.fTheoryRtr_km = 0
        self.fTheoryRmin_km = 0
        self.fTheoryRmax_km = 0
        self.fDisAlterRate = 0
        self.fDis = 0
        self.nDLTargetLot = 0


class PlaneSituationModelAIMInfoBack:
    def __init__(self):
        self.PL15_bValid = 0
        # self.PL15_nLot = 0
        self.nDLRecvFlag = 0
        self.bTrackingFlag = 0
        self.bSeekerHPFlag = 0
        self.bDataLineState = 0

        self.PL15_nLot = 0

        self.fVx = 0
        self.fVy = 0
        self.fVz = 0
        self.fXe = 0
        self.fYe = 0
        self.fZe = 0
        self.fMTDistance = 0


class AlarmInfo:
    def __init__(self):
        self.AlarmInfo_bValid = 0
        self.nTargetType = 0
        self.nLot = 0
        self.nEWLot = 0
        self.bEWAdvise1 = 0
        self.bEWAdvise2 = 0
        self.bEWAdvise3 = 0
        self.bEWAdvise4 = 0
        self.bJamState1 = 0
        self.bJamState2 = 0
        self.bJamState3 = 0
        self.bJamState4 = 0
        self.fTargetRaero = 0
        self.fTargetRtr = 0
        self.nTargetEnvelopeType = 0
        self.nIdentify = 1
        self.nPlatformType = 0
        self.nWeaponType = 0
        self.bWarnMslNearing = 0
        self.bWarnMslLaunched = 0
        self.nIdentifyResults = 0
        self.fDis = 0
        self.fMisAzi = 0
        # self.fMisEle = 0


class PlaneSituationModel:
    def __init__(self):
        self.nTargetDataListNum = 0

        self.aaTargetData = []

        self.SMSInfo_bValid = 0
        self.bMainWpnState = 0
        self.bAssWpnState = 0
        self.nAAMMissileNum = 0
        self.nSAAMMissileNum = 0
        self.fFuelInPlane_kg = 0
        self.FCMInfo_bValid = 0
        self.nLot = 0
        self.fTargetMach_M = 0
        self.fTargetAlt_m = 0
        self.fTargetDis_km = 0
        self.fDisAlterRate_ms = 0
        self.fEnterAngle_rad = 0
        self.sFCMRDM_bValid = 0
        self.fRaero_km = 0
        self.fRopt_km = 0
        self.fRpi_km = 0
        self.sFCMRDM_fRtr_km = 0
        self.fRacue_km = 0
        self.sFCMRDM_fRmin_km = 0
        self.sFCMRDM_fRmax_km = 0
        self.fAFPole_km = 0
        self.fDMC_deg = 0
        self.fOperatingDotAzim_rad = 0
        self.fOperatingDotPitch_rad = 0
        self.fOperatingCirleDiameter_rad = 0
        self.fClimAgl_deg = 0
        self.fPreLanuchTime_s = 0
        self.fMPI = 0
        self.nAttackIndication = 0
        self.sFCMIRM_bValid = 0
        self.sFCMIRM_fRmax_km = 0
        self.sFCMIRM_fRmin_km = 0
        self.sFCMIRM_fRtr_km = 0
        self.fSeekerAzim_rad = 0
        self.fSeekerPitch_rad = 0
        self.fSeekerAzimP_rad = 0
        self.fSeekerPitchP_rad = 0
        self.sFCMIRM_nAttackIndication = 0
        self.bIsTracked = 0
        self.bIsOverMaxOffAxisAgl = 0
        self.nMslPropertyNum = 0

        self.sMslProperty = []

        self.nAvionicsMode = 0
        self.nAEPowerByDL = 0
        self.nRadiateManager = 0
        self.bICNIPower = 0
        self.bJIDSPower = 0
        self.bEWSPower = 0
        self.bAEPower = 0
        self.bOEDEPower = 0
        self.nAEWorkMode = 0
        self.bAEIsRadiate = 0
        self.bIsHPECM = 0
        self.bIsFireHPECM = 0
        self.nAEOPState = 0
        self.nAEACMMode = 0
        self.bAETargetAbort = 0
        self.bAESTAS = 0
        self.bAESTT = 0
        self.nAEAADisMeasure = 0
        self.nAESphereSelect = 0
        self.nAETargetVelThreshold = 0
        self.bAEFakeGuideSignal = 0
        self.nAEAAScanLines = 0
        self.nAEAAScanScale = 0
        self.fAEScanCenterAzim_rad = 0
        self.fAEScanCenterPitch_rad = 0
        self.nEWWorkMode = 0
        self.bIsCanRadiate = 0
        self.bHPECMAsk = 0
        self.bHighPresure = 0
        self.bLaunchBait = 0
        self.bWarnMslNearing = 0
        self.bWarnMslLaunched = 0
        self.nLeftFrontRadiation = 0
        self.nRightFrontRadiation = 0
        self.nBackRadiation = 0
        self.nPJammProSelect = 0
        self.bIsProCanSelect = [0] * 7
        self.bFlame = [0] * 3
        self.bIsLeftValid = 0
        self.nBaitLeftState = 0
        self.nBaitLeftLaunchState = 0
        self.bIsRightValid = 0
        self.nBaitRightState = 0
        self.nBaitRightLaunchState = 0
        self.nOEDEWorkState = 0
        self.nOETrackMethod = 0
        self.nOELaserState = 0
        self.nOETrackingState = 0
        self.bOELaserRadiate = 0
        self.nOEAzimScanRange = 0
        self.nOEPitchScanRange = 0
        self.nMainWpnType = 0
        self.nTargetAlloc = [0] * 3
        self.nAllyNo = 0
        self.nRCSType = 0
        self.nRCSType_Auto = 0
        self.nChaffLeftNum = 0
        self.nFlameLeftNum = 0
        self.bActiveBaitDropAdvise = 0
        self.nAIMInfoInfoNum = 0

        self.sAIMInfo = []

        self.nTargetInListNum = 0

        self.sTargetInListData = []

        self.fRealAzimuth_rad_rad = 0
        self.fMagneticAzimuth_rad = 0
        self.fGroundSpeed_ms = 0
        self.fDriftAngle_rad = 0
        self.fHorizontalTrackAngle_rad = 0
        self.fWindSpeed_ms = 0
        self.fWindDirection = 0
        self.dLongtitude_rad = 115
        self.dLatitude_rad = 30
        self.fAltitude_m = 0
        self.fHeading_rad = 0
        self.fPitch_rad = 0
        self.fRoll_rad = 0
        self.fVn_ms = 0
        self.fVu_ms = 0
        self.fVe_ms = 0
        self.fAccN_ms2 = 0
        self.fAccU_ms2 = 0
        self.fAccE_ms2 = 0
        self.fAbsAlt_m = 0
        self.fRadioAlt_m = 0
        self.fRealAirspeed_kmh = 0
        self.fCalibratedAlt_m = 0
        self.fMach_M = 0
        self.fCAS_kmh = 0
        self.fNormalAcc_g = 0
        self.fVTrackAngle_rad = 0
        self.fMaxAttackAngle_rad = 0
        self.fMinAttackAngle_rad = 0
        self.fMaxCAS_kmh = 0
        self.fMinCAS_kmh = 0
        self.fMaxMach_M = 0
        self.fMaxNormalOverload_g = 0
        self.fMinNormalOverload_g = 0
        self.bOver = 0
        self.nEndReason = 0
        self.fAggregateScore = 0
        self.fReward = 0
        self.nAlarmNum = 0

        self.sAlarmInfo = []

        self.nHitFighterWeaponLot = 0
        self.nHitTargetWeaponLot = 0
        self.dTimeStamp = 0.0
        self.iCmdIndex = 0
        self.iCmdID = 0


# Fiona add begin
class PlaneErrorStatusInfo:
    def __init__(self):
        self.key = ''
        self.value = 0
        self.range = []
# Fiona add end
