from ctypes import *


class SOOperation(Structure):
    _fields_ = [
        ("nAvionicsMode", c_int),
        ("nRadiateManagement", c_int),
        ("nMainWpnSelect", c_int),
        ("nAssWpnSelect", c_int),
        ("nPL15PrepareOrder", c_int),
        ("nMslTargetRatioPL15", c_int),
        ("nNTSIdAssigned", c_int),
        ("nTargetOPInAtkList", c_int),
        ("nAEWorkState", c_int),
        ("bLockOnNTS", c_bool),
        ("nAEOPState", c_int),
        ("nACMMode", c_int),
        ("bOETargetAbort", c_bool),
        ("bNTSAssigned", c_bool),
        ("bHPECM", c_bool),
        ("bFCM_HPECM", c_bool),
        ("nAEAADisMeasure", c_int),
        ("nAESphereSelect", c_int),
        ("nAETargetVelThreshold", c_int),
        ("bAEFakeGuideSignal", c_bool),
        ("nAEAAScanLines", c_int),
        ("nAEAAScanScale", c_int),
        ("nAEFreqPointNo", c_int),
        ("nEWWorkMode", c_int),
        ("nEWRadiateControl", c_int),
        ("HGESMScanRange", c_int),
        ("nActiveJamDirSelect", c_int),
        ("nJamTypeSelect", c_int),
        ("nProgramSelect", c_int),
        ("nLaunchType", c_int),
        ("bLaunchBait", c_bool),
        ("nOEOPMode", c_int),
        ("bOETrackOrder", c_bool),
        ("nOETrackMethod", c_int),
        ("nOELaserOrder", c_int),
        ("bOEBackToScan", c_bool),
        ("nOEAzimRange", c_int),
        ("nOEPitchRange", c_int),
        ("nOETrackingLot", c_int),
        ("fOETargetAssignedAzim_rad", c_float),
        ("fOETargetAssignedPitch_rad", c_float),
        ("nRCSType", c_int),
    ]


class ScanCenterControl(Structure):
    _fields_ = [
        ("bAEScanCenterValid", c_bool),
        ("bOETargetAgnValid", c_bool),
        ("bOEScanCenterValid", c_bool),
        ("fAEScanCenterAzim_rad", c_float),
        ("fAEScanCenterPitch_rad", c_float),
        ("fOEScanCenterAzim_rad", c_float),
        ("fOEScanCenterPitch_rad", c_float),
    ]


class PlaneControl(Structure):
    _fields_ = [
        ("dForceLat", c_double),
        ("dForcePedal", c_double),
        ("dForceLong", c_double),
        ("iPitchTrim", c_int),
        ("iRollTrim", c_int),
        ("iYawTrim", c_int),
        ("fThrottlePosition", c_double),
        ("fSpeedBrake", c_double),
        ("iAPModePitch", c_int),
        ("iAPModeRoll", c_int),
        ("fWindSpeedX", c_double),
        ("fWindSpeedY", c_double),
        ("fWindSpeedZ", c_double),
        ("iCmdIndex", c_short),
        ("iCmdID", c_ushort),
        ("bApplyNow", c_bool),
        ("iVelType", c_ushort),
        ("fCmdNy", c_float),
        ("fCmdSpd", c_float),
        ("fCmdAlt", c_float),
        ("fCmdPhi", c_float),   
        ("iTurnDirection", c_short), 
        ("fCmdDeltaHeading", c_float),  
        ("fTime", c_float),
        ("fCmdThrust", c_float),
        ("fThrustLimit", c_float),
        ("fCmdPitchDeg", c_float),
        ("fCmdHeadingDeg", c_float),
        ("fCmdObliqueDeg", c_float), 
        ("fCmdBdyPitchDeg", c_float), 
        ("fCmdBdyPsiDeg", c_float), 
        ("fCmdRollDeg", c_float),
        ("fLimitAlt", c_float), 
        ("fLimitVc", c_float), 
    ]


class OtherControl(Structure):
    _fields_ = [
        ("bLaunch", c_bool),
    ]


class AIInputData(Structure):
    _fields_ = [
        ("sSOCtrl", SOOperation),
        ("sScanCenter", ScanCenterControl),
        ("siPlaneControl", PlaneControl),
        ("sOtherControl", OtherControl),
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
        ("h_change", c_int),
        ("JS", c_int),
        ("time", c_float),
        ("iEvade", c_int),
        ("evadeT", c_float),
        ("crankH", c_float),
        ("bLockOnNTS", c_bool),
        ("bAssignNTS", c_bool),
        ("sttTime", c_float),
        ("tasTime", c_float),
        ("tarLotNum", c_int),
        ("tarLot", c_int),
        ("pointNum", c_int),
        ("lastpointTime", c_float),
        ("jsCount", c_int),
        ("abortTime", c_float),
        ("iTurnDirection", c_int),
        ("loftBz", c_bool),
        ("loftAngle", c_float),
        ("lastSms", c_int),
        ("tsJudge", c_int),
        ("safeTime", c_float),
        ("evadeSt", c_int),
    ]

class DecisionData(Structure):
    _fields_ = [
        ("stage", c_int),
        ("M_No_p", c_int),
        ("shoot_p", c_bool),
        ("LZ", c_int),
        ("Cindex", c_int),
        ("h_dive", c_float),
        ("h_climb", c_float),
        ("h_change", c_int),
        ("JS", c_int),
        ("time", c_float),
        ("iEvade", c_int),
        ("evadeT", c_float),
        ("crankH", c_float),
        ("bLockOnNTS", c_bool),
        ("bAssignNTS", c_bool),
        ("sttTime", c_float),
        ("tasTime", c_float),
        ("tarLotNum", c_int),
        ("tarLot", c_int),
        ("pointNum", c_int),
        ("lastpointTime", c_float),
        ("jsCount", c_int),
        ("abortTime", c_float),
		("beamTime", c_float),
        ("iTurnDirection", c_int),
        ("loftBz", c_bool),
        ("loftAngle", c_float),
        ("lastSms", c_int),
        ("tsJudge", c_int),
        ("safeTime", c_float),
        ("evadeSt", c_int)
    ]
