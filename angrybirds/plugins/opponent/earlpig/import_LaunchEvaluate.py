import sys
from angrybirds.config.sim_env_config import EarlPigPath
sys.path.append(EarlPigPath)
from evaluate import LaunchEvaluate
import os


class ImportLaunchEvaluate:

    def __init__(self):
        cmd = "cp -r " + EarlPigPath + "libs/ ./"
        os.system(cmd)
        self.evaluate = LaunchEvaluate()

    def __del__(self):
        cmd = "rm -rf " + "./libs"
        os.system(cmd)
        del cmd