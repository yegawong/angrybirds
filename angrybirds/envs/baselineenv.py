#!/usr/bin/python
""" BaselineEnv Class """
import math
from angrybirds.envs.slingshot import Slingshot
from angrybirds.config.plane_config import EnvConfig
from angrybirds.plugins.opponent.opponent_interface_kf import OpponentInterface
# @TODO if gbz has baseline opponent, use this
# from angrybirds.plugins.opponent.opponent_interface import OpponentInterface
from angrybirds.config.sim_env_config import BechmarkOpponentL1ExamPath
from angrybirds.config.sim_env_config import BechmarkOpponentL2ExamPath


class BaselineEnv(Slingshot):

    def __init__(self, log_level='ERROR', select_side='BLUE', opponent='Mauro'):
        EnvConfig.beat = math.gcd(EnvConfig.red_beat, EnvConfig.blue_beat)
        self.deltabeat = EnvConfig.beat
        self.gamebeat = max(EnvConfig.red_beat, EnvConfig.blue_beat)
        self.select_obs_idx = 0 if select_side.upper() == 'BLUE' else 1
        if 'Nigel' == opponent:
            self.opponent_path = BechmarkOpponentL1ExamPath
        elif 'Mauro' == opponent:
            self.opponent_path = BechmarkOpponentL2ExamPath
        else:
            self.opponent_path = BechmarkOpponentL1ExamPath
        super().__init__(log_level=log_level)

    def reset(self):
        self.tree_eval = OpponentInterface(self.opponent_path, self.select_obs_idx + 1, EnvConfig.beat)
        self.obs = None
        self.__tree_eval_action = None
        self.__isset__ = False
        self.obs, rew, done, info = super().reset()
        return self.obs, rew, done, info

    def set_tree_eval_action(self, action: object):
        self.__tree_eval_action = action
        self.__isset__ = True

    def get_tree_eval_action(self):
        self.__tree_eval_action = self.tree_eval.data_interactive(self.obs[self.select_obs_idx])
        self.__isset__ = False
        return self.__tree_eval_action

    def step(self, action: object):
        for _ in range(0, self.gamebeat, self.deltabeat):
            tree_eval_action = self.__tree_eval_action if self.__isset__ else self.get_tree_eval_action()
            actions = [tree_eval_action, action] if self.select_obs_idx == 0 else [action, tree_eval_action]
            self.obs, rw, done, info = super().step(actions)
            if done is True:
                break
            if info['crash'] is True:
                break
        return self.obs, rw, done, info
