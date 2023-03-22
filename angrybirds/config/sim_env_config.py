from angrybirds.lib.util import get_username
from angrybirds.config.plane_config import EnvConfig
import os
# NOTE: If you know you're running this on the docker, you can just
# use "$HOME" here.
if ("PLUGIN_EXE" in os.environ
        and not os.environ["PLUGIN_EXE"] == ""):
    HOMEPATH = os.environ["PLUGIN_EXE"]
else:
    HOMEPATH = os.environ["HOME"]
Qt_version = '5.5.1'
PluginExeWorkPath = HOMEPATH + '/plugin_exe/package/'
PluginExeProgressName = ['MainController', 'FCSPlatform', 'DebugLogServer', 'StateLogServer']
PluginExeTmpFlag = 'fcsystem'
PluginExeTmpFilePath = ['/dev/shm/', '/tmp/']
PluginExeServerPort = ['60000', '60001']
PluginExeCommand = PluginExeWorkPath + "MainController 1 60000 " + PluginExeTmpFlag + " " + str(
    EnvConfig.plane_count) + " " + str(EnvConfig.log_level)
PluginExeTxtFlag = "/tmp/start.txt"
PluginExeInitTimeout = 10
PluginExeTimeout = 60
PluginExeControlTimeout = 60
PluginExeAuthServer = "fit.domocloud.cn"
PluginExeAuthINIPath = PluginExeWorkPath + "MainController.ini"
BechmarkOpponentPath = PluginExeWorkPath + "opponent/"
BechmarkOpponentL1Path = BechmarkOpponentPath + "libTreeEval_no.so"
BechmarkOpponentL2Path = BechmarkOpponentPath + "libTreeEval_yes.so"
BechmarkOpponentL1ExamPath = BechmarkOpponentPath + "exam_libTreeEval_no.so"
BechmarkOpponentL2ExamPath = BechmarkOpponentPath + "exam_libTreeEval_yes.so"
EarlPigPath = PluginExeWorkPath + "opponent/earlpig/"
EarlPigOpponentPath = EarlPigPath + "/libs/libTreeEval_a.so"
EarlPig_sync_buffer_Path = BechmarkOpponentPath + "sync_buffer.so"
EarlPig_evaluate_Path = BechmarkOpponentPath + "evaluate.so"
EarlPig_key_event_recorder_Path = BechmarkOpponentPath + "key_event_recorder.so"
EarlPig_main_logic_Path = BechmarkOpponentPath + "main_logic.so"
