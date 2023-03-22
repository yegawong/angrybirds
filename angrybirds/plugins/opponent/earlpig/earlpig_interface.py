import sys
import os
from ctypes import (cdll, POINTER, byref, c_int)
from .earlpig_situation_decode import (AIData, decision_data, PlaneSituationDecoder,
                                       situation_to_old_situation)
from .plane_action_model import PlaneActionModel
from angrybirds.config.sim_env_config import EarlPigPath
from angrybirds.plugins.opponent.plane_action_opponent import AIInputData as opponent_AIInputData
sys.path.append(EarlPigPath)


class OpponentInterface():

    def __init__(self, path, plane_id, plane_beat):
        from key_event_recorder import KeyEventRecorder
        from .import_LaunchEvaluate import ImportLaunchEvaluate
        from main_logic import MainLogic
        # from sync_buffer import SyncBuffer
        self.plane_id = plane_id
        self.plane_beat = plane_beat
        dll = cdll.LoadLibrary(path)
        self.tree_eval = dll.tree_eval
        # set the return type
        self.tree_eval.argtypes = [
            AIData, POINTER(decision_data),
            POINTER(opponent_AIInputData), c_int, c_int
        ]
        # self.sync_buffer = SyncBuffer()
        self.key_event_recorder = KeyEventRecorder()
        self.evaluate = ImportLaunchEvaluate().evaluate
        self.main_logic = MainLogic()
        self.info_dict = {'MCLaunched': False, 'version': 0}
        self.step = 0
        self.ptd_situation_decoder = PlaneSituationDecoder()

    def data_interactive(self, obs: list):
        """
        data interactive situation -> AI
        :param situation: from simulator to AI
        :return: action: from AI to simulator
        """
        self.step += 1
        plane_id = 1
        red_situation = obs[0]
        blue_situation = obs[-1]
        red_rule_input = situation_to_old_situation(red_situation)
        blue_rule_input = situation_to_old_situation(blue_situation)
        red_ptd_situation = self.ptd_situation_decoder.old_sitiuation_to_ptd_model(red_rule_input)
        blue_ptd_situation = self.ptd_situation_decoder.old_sitiuation_to_ptd_model(blue_rule_input)
        # self.sync_buffer.set_red_plane_situation(plane_situation_model)
        # self.sync_buffer.set_step(self.step)
        plane_self, plane_enenmy = self.ptd_situation_decoder.decode_AIAlgo(blue_ptd_situation)
        self.key_event_recorder.record_event(blue_ptd_situation, red_ptd_situation, self.step)
        self.evaluate.get_vseq(plane_self, plane_enenmy, self.key_event_recorder, plane_id)
        plane_action_model = PlaneActionModel()
        plane_action_model.iCmdID = 1
        plane_action_model.fCmdHeadingDeg = -500
        plane_action_model.fThrustLimit = 120
        plane_action_model.fCmdSpd = 0
        plane_action_model.iVelType = 0
        plane_action_model.bAEFakeGuideSignal = 0
        plane_action_model.nEWRadiateControl = 0

        if self.info_dict['version'] == 2:
            rule_output = self.combat_rule(blue_rule_input, self.tree_eval)
        else:
            if blue_ptd_situation.nTargetDataListNum != 0:
                self.main_logic.main_process(blue_ptd_situation, plane_action_model, self.info_dict,
                                             self.key_event_recorder)
                if self.main_logic.bValid:  # Get MC/Alpha Algo's Privilege
                    plane_action_model.bLaunch = True  # MC/Alpha Algo Process　# 这里需要修改一个参数进去
                    self.info_dict[
                        "MCLaunched"] = True  # Set whether the MC/Alpha algo launch the missle
            if blue_ptd_situation.nTargetDataListNum == 0:
                plane_action_model.bLaunch = False
            rule_output = self.ptd_to_action(plane_action_model)

        return rule_output

    def combat_rule(self, rule_input, tree_eval):
        ds_data = decision_data()
        rule_output = opponent_AIInputData()
        # invoke api tree_eval
        retStr = tree_eval(rule_input, byref(ds_data), byref(rule_output), 0, 1)
        return rule_output

    def get_evaluate(self):
        return [
            self.evaluate.v_LSTM["rew_dw"][0],
            self.evaluate.v_LSTM["rew_dw"][1],
            self.evaluate.v_LSTM["rew_dw"][2],
            self.evaluate.v_LSTM["rew_dw"][3],
            self.evaluate.v_LSTM["rew_dv"][0],
            self.evaluate.v_LSTM["rew_dv"][1],
            self.evaluate.v_LSTM["rew_dv"][2],
            self.evaluate.v_LSTM["rew_dv"][3],
            self.evaluate.v_LSTM["rew_wv"][0],
            self.evaluate.v_LSTM["rew_wv"][1],
            self.evaluate.v_LSTM["rew_wv"][2],
            self.evaluate.v_LSTM["rew_wv"][3],
            self.evaluate.v_LSTM["rew_vtd"],
        ]

    def ptd_to_action(self, output_value):
        rule_output = opponent_AIInputData()
        rule_output.sOtherControl.bLaunch = output_value.bLaunch

        rule_output.siPlaneControl.iCmdID = output_value.iCmdID
        rule_output.siPlaneControl.iCmdIndex = output_value.iCmdIndex
        rule_output.siPlaneControl.bApplyNow = output_value.bApplyNow
        rule_output.siPlaneControl.iVelType = output_value.iVelType
        rule_output.siPlaneControl.fCmdNy = output_value.fCmdNy
        rule_output.siPlaneControl.fCmdSpd = output_value.fCmdSpd
        rule_output.siPlaneControl.fCmdAlt = output_value.fCmdAlt
        rule_output.siPlaneControl.fCmdPitchDeg = output_value.fCmdPitchDeg
        rule_output.siPlaneControl.fCmdRollDeg = output_value.fCmdRollDeg
        rule_output.siPlaneControl.iTurnDirection = output_value.iTurnDirection
        rule_output.siPlaneControl.fCmdHeadingDeg = output_value.fCmdHeadingDeg
        rule_output.siPlaneControl.fCmdDeltaHeading = output_value.fCmdDeltaHeading
        rule_output.siPlaneControl.fTime = output_value.fTime
        rule_output.siPlaneControl.fCmdThrust = output_value.fCmdThrust
        rule_output.siPlaneControl.fThrustLimit = output_value.fThrustLimit

        rule_output.sSOCtrl.nRadiateManagement = output_value.nRadiateManagement
        rule_output.sSOCtrl.nMainWpnSelect = output_value.nMainWpnSelect
        rule_output.sSOCtrl.nNTSIdAssigned = output_value.nNTSIdAssigned
        rule_output.sSOCtrl.nAEOPState = output_value.nAEOPState
        if rule_output.sSOCtrl.nAEOPState == 2:
            rule_output.sSOCtrl.nAEOPState = 5
        elif rule_output.sSOCtrl.nAEOPState == 5:
            rule_output.sSOCtrl.nAEOPState = 2
        rule_output.sSOCtrl.bNTSAssigned = output_value.bNTSAssigned
        rule_output.sSOCtrl.bLockOnNTS = output_value.bLockOnNTS
        rule_output.sSOCtrl.nAEAADisMeasure = output_value.nAEAADisMeasure
        rule_output.sSOCtrl.nAEAAScanLines = output_value.nAEAAScanLines
        rule_output.sSOCtrl.nAEAAScanScale = output_value.nAEAAScanScale
        rule_output.sSOCtrl.nAEFreqPointNo = output_value.nAEFreqPointNo
        rule_output.sSOCtrl.nEWRadiateControl = output_value.nEWRadiateControl
        rule_output.sSOCtrl.nJamTypeSelect = output_value.nJamTypeSelect
        rule_output.sSOCtrl.bLaunchBait = output_value.bLaunchBait
        rule_output.sSOCtrl.nRCSType = output_value.nRCSType
        rule_output.sScanCenter.bAEScanCenterValid = output_value.bAEScanCenterValid
        rule_output.sScanCenter.bOETargetAgnValid = output_value.bOETargetAgnValid
        rule_output.sScanCenter.bOEScanCenterValid = output_value.bOEScanCenterValid
        rule_output.sScanCenter.fAEScanCenterAzim_rad = output_value.fAEScanCenterAzim_rad
        rule_output.sScanCenter.fAEScanCenterPitch_rad = output_value.fAEScanCenterPitch_rad
        return rule_output
