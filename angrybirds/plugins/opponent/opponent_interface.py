from ctypes import cdll
from ctypes import *
from angrybirds.plugins.opponent.plane_situation_opponent import AIData
from angrybirds.plugins.opponent.plane_action_opponent import AIInputData, decision_data, DecisionData


class OpponentInterface():

    def __init__(self, path, plane_id, plane_beat):
        self.plane_id = plane_id
        self.plane_beat = plane_beat
        dll = cdll.LoadLibrary(path)
        self.tree_eval = dll.tree_eval
        self.tree_eval.argtypes = [
            AIData, POINTER(DecisionData),
            POINTER(AIInputData), c_int, c_int, c_int
        ]
        self.ds_data = DecisionData()
        # # set the return type
        # if model.upper() == "EXAM":
        #     self.tree_eval.argtypes = [
        #         AIData, POINTER(DecisionData),
        #         POINTER(AIInputData), c_int, c_int, c_int
        #     ]
        #     self.ds_data = DecisionData()
        # else:   # TRAIN
        #     self.tree_eval.argtypes = [
        #         AIData, POINTER(decision_data),
        #         POINTER(AIInputData), c_int, c_int, c_int
        #     ]
        #     self.ds_data = decision_data()
        self.rule_input = AIData()
        self.rule_output = AIInputData()

    def data_interactive(self, situation: AIData):
        """
        data interactive situation -> AI
        :param situation: from simulator to AI
        :return: action: from AI to simulator
        """
        self.rule_input = situation
        # invoke api tree_eval
        retStr = self.tree_eval(self.rule_input, byref(self.ds_data), byref(self.rule_output), 0,
                                self.plane_id, self.plane_beat)
        return self.rule_output
