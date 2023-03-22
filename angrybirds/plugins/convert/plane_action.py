#!/usr/bin/env python3
""" Parent class for plane action data structure """
""" AI >>>> simtuation """
from angrybirds.lib.structure import Structure


class SOOperation(Structure):
    _fields_ = [
        ('<i', 'nAvionicsMode'),
        ('i', 'nRadiateManagement'),
        ('i', 'nMainWpnSelect'),
        ('i', 'nAssWpnSelect'),
        ('i', 'nPL15PrepareOrder'),
        ('i', 'nMslTargetRatioPL15'),
        ('i', 'nNTSIdAssigned'),
        ('i', 'nTargetOPInAtkList'),
        ('i', 'nAEWorkState'),
        ('?', 'bLockOnNTS'),
        ('i', 'nAEOPState'),
        ('i', 'nACMMode'),
        ('?', 'bOETargetAbort'),
        ('?', 'bNTSAssigned'),
        ('?', 'bHPECM'),
        ('?', 'bFCM_HPECM'),
        ('i', 'nAEAADisMeasure'),
        ('i', 'nAESphereSelect'),
        ('i', 'nAETargetVelThreshold'),
        ('?', 'bAEFakeGuideSignal'),
        ('i', 'nAEAAScanLines'),
        ('i', 'nAEAAScanScale'),
        ('i', 'nAEFreqPointNo'),
        ('i', 'nEWWorkMode'),
        ('i', 'nEWRadiateControl'),
        ('i', 'HGESMScanRange'),
        ('i', 'nActiveJamDirSelect'),
        ('i', 'nJamTypeSelect'),
        ('i', 'nProgramSelect'),
        ('i', 'nLaunchType'),
        ('?', 'bLaunchBait'),
        ('i', 'nOEOPMode'),
        ('?', 'bOETrackOrder'),
        ('i', 'nOETrackMethod'),
        ('i', 'nOELaserOrder'),
        ('?', 'bOEBackToScan'),
        ('i', 'nOEAzimRange'),
        ('i', 'nOEPitchRange'),
        ('i', 'nOETrackingLot'),
        ('f', 'fOETargetAssignedAzim_rad'),
        ('f', 'fOETargetAssignedPitch_rad'),
        ('i', 'nRCSType'),
    ]


class ScanCenterControl(Structure):
    _fields_ = [
        ('?', 'bAEScanCenterValid'),
        ('?', 'bOETargetAgnValid'),
        ('?', 'bOEScanCenterValid'),
        ('f', 'fAEScanCenterAzim_rad'),
        ('f', 'fAEScanCenterPitch_rad'),
        ('f', 'fOEScanCenterAzim_rad'),
        ('f', 'fOEScanCenterPitch_rad'),
    ]


class PlaneControl(Structure):
    _fields_ = [
        ('d', 'dForceLat'),
        ('d', 'dForcePedal'),
        ('d', 'dForceLong'),
        ('i', 'iPitchTrim'),
        ('i', 'iRollTrim'),
        ('i', 'iYawTrim'),
        ('d', 'fThrottlePosition'),
        ('d', 'fSpeedBrake'),
        ('i', 'iAPModePitch'),
        ('i', 'iAPModeRoll'),
        ('d', 'fWindSpeedX'),
        ('d', 'fWindSpeedY'),
        ('d', 'fWindSpeedZ'),
        ('h', 'iCmdIndex'),
        ('H', 'iCmdID'),
        ('?', 'bApplyNow'),
        ('H', 'iVelType'),
        ('f', 'fCmdNy'),
        ('f', 'fCmdSpd'),
        ('f', 'fCmdAlt'),
        ('f', 'fCmdPhi'),
        ('h', 'iTurnDirection'),
        ('f', 'fCmdDeltaHeading'),
        ('f', 'fTime'),
        ('f', 'fCmdThrust'),
        ('f', 'fThrustLimit'),
        ('f', 'fCmdPitchDeg'),
        ('f', 'fCmdHeadingDeg'),
        ('f', 'fCmdObliqueDeg'),
        ('f', 'fCmdBdyPitchDeg'),
        ('f', 'fCmdBdyPsiDeg'),
        ('f', 'fCmdRollDeg'),
        ('f', "fLimitAlt"),
        ('f', "fLimitVc"),
    ]


class OtherControl(Structure):
    _fields_ = [
        ('?', 'bLaunch'),
    ]


class AIInputData(Structure):
    _fields_ = [
        (SOOperation, 'sSOCtrl'),
        (ScanCenterControl, 'sScanCenter'),
        (PlaneControl, 'siPlaneControl'),
        (OtherControl, 'sOtherControl'),
    ]


class AIIputDataDefaultValue:
    default_value = {
        'sSOCtrl': {
            'nAvionicsMode': 3,
            'nRadiateManagement': 1,
            'nMainWpnSelect': 13,
            'nAssWpnSelect': 13,
            'bLockOnNTS': False,
            'nAEOPState': 5,
            'nAEAADisMeasure': 6,
            'nAESphereSelect': 1,
            'bAEFakeGuideSignal': False,
            'nAEAAScanLines': 2,
            'nAEAAScanScale': 3,
            'nEWRadiateControl': 1,
            'nActiveJamDirSelect': 1,
            'nJamTypeSelect': 4,
            'nProgramSelect': 1,
            'bLaunchBait': False,
            'bOETrackOrder': False,
            'bOEBackToScan': False,
            'bAEScanCenterValid': False,
            'bOETargetAgnValid': False,
            'bOEScanCenterValid': False,
        },
        'siPlaneControl': {
            'bApplyNow': True,
            'fCmdNy': 1,
            'fThrustLimit': 120,
        },
        'sOtherControl': {
            'bLaunch': False,
        },
    }
