#!/usr/bin/python
""" SelfplayEnv Class """
from angrybirds.envs.slingshot import Slingshot
from angrybirds.config.plane_config import EnvConfig


class SelfplayEnv(Slingshot):

    def __init__(self, log_level='ERROR'):
        EnvConfig.beat = max(EnvConfig.red_beat, EnvConfig.blue_beat)
        super().__init__(log_level=log_level)
