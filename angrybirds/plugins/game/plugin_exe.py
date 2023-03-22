#!/usr/bin/env python3
""" Parent class for plane simuation exe"""
import os
import time
import signal
import subprocess
import logging
import json
from angrybirds.config.sim_env_config import PluginExeWorkPath
from angrybirds.config.sim_env_config import Qt_version
from angrybirds.config.sim_env_config import PluginExeProgressName
from angrybirds.config.sim_env_config import PluginExeTmpFlag
from angrybirds.config.sim_env_config import PluginExeTmpFilePath
from angrybirds.config.sim_env_config import PluginExeServerPort
from angrybirds.config.sim_env_config import PluginExeCommand
from angrybirds.config.sim_env_config import PluginExeTxtFlag
from angrybirds.config.sim_env_config import PluginExeAuthINIPath
from angrybirds.config.sim_env_config import PluginExeAuthServer
from angrybirds.config.sim_env_config import PluginExeInitTimeout
from angrybirds.config.plane_config import IEWS_HX
from angrybirds.config.plane_config import RADAR_HX
from angrybirds.config.plane_config import EnvConfig
from angrybirds.lib import util
from angrybirds.lib.error import QtNotFoundError, FlagTxtCreateError, QtVersionError, StartExeError
logger = logging.getLogger(__name__)


class PluginExe:

    def __init__(self):
        logger.debug("Initializing %s", self.__class__.__name__)
        self.process = None
        # self._check_require()
        logger.debug("Initialized %s", self.__class__.__name__)

    def start_exe(self):
        logger.debug("[CMD_START]")
        # self.generate_ini()
        self.generate_unique_sign()
        profile = self.generate_os_profile()
        self.process = subprocess.Popen(
            PluginExeCommand,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            cwd=PluginExeWorkPath,
            env=profile,
        )
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        while not util.check_port(PluginExeServerPort[0]):
            if delta_time > PluginExeInitTimeout:
                raise StartExeError("start exe timeout")
            res = subprocess.Popen.poll(self.process)
            if res is None:
                time.sleep(0.1)
            else:
                out, err = self.process.communicate()
                raise StartExeError("execute exe failed, %s %s" % (out, err))
            end_time = time.perf_counter()
            delta_time = end_time - start_time
        with open(os.devnull, 'w') as devnull:
            self.process.stdout = devnull
            self.process.stderr = devnull
        logger.info("wait plugin_exe have 4 second delay ...")
        time.sleep(4)  # wait plugin_exe have 4 second delay
        logger.debug("'{}' [CMD_START]".format(self.process.pid))

    def stop_exe(self):
        self.remove_state_file()
        self.remove_log_file()
        if self.process is not None:
            self.process.kill()
        logger.debug("kill plugin exe process")
        for process_name in PluginExeProgressName:
            self.kill_process(process_name)
        logger.debug("kill plugin exe system process")
        self.remove_file(PluginExeTxtFlag)
        logger.debug("remove file PluginExeTxtFlag")
        for filepath in PluginExeTmpFilePath:
            self.remove_tmpfile(filepath)
        logger.debug("remove file PluginExeTmpFilePath")
        for port in PluginExeServerPort:
            self.kill_port(port)
        logger.debug("kill port PluginExeServerPort")
        logger.debug("[CMD_STOP]")

    def generate_unique_sign(self):
        cmd = "echo %s > %s" % (PluginExeTmpFlag, PluginExeTxtFlag)
        status, output = subprocess.getstatusoutput(cmd)
        if status != 0:
            raise FlagTxtCreateError("%s create failed" % PluginExeTxtFlag)

    def generate_os_profile(self):
        profile = dict(os.environ)
        if 'LD_LIBRARY_PATH' in profile:
            profile['LD_LIBRARY_PATH'] = PluginExeWorkPath + "base:" + profile['LD_LIBRARY_PATH']
        else:
            profile['LD_LIBRARY_PATH'] = PluginExeWorkPath + "base"
        return profile

    def generate_ini(self):
        cmdlist = []
        cmdlist.append("[MainControllerConfig]")
        cmdlist.append("EN_SETTING_ID_SIMULATION_TIMER=20\\n")
        cmdlist.append("EN_SETTING_ID_SIMULATION_SYNC_STEP=100\\n")
        cmdlist.append("EN_SETTING_ID_INTEGRITY_SERVER_IP=127.0.0.1\\n")
        # res, auth_ip = util.get_domain_host(PluginExeAuthServer)
        # if not res or not util.check_port(55555, PluginExeAuthServer):
        #     from angrybirds.plugins.game.auth_sever import auth_server
        #     auth_server(host="127.0.0.1", port=55555)
        #     cmdlist.append("EN_SETTING_ID_INTEGRITY_SERVER_IP=127.0.0.1\\n")
        # else:
        #     cmdlist.append("EN_SETTING_ID_INTEGRITY_SERVER_IP=%s\\n" % auth_ip)
        cmdlist.append("EN_SETTING_ID_INTEGRITY_SERVER_PORT=55555\\n")
        with open(PluginExeAuthINIPath, 'w') as f:
            for cmd in cmdlist:
                f.write(cmd)
                f.write("\n")

    def _check_require(self):
        res, version = util.check_qt(Qt_version)
        if not res:
            if version is None:
                raise QtNotFoundError("Not Found Qt:", Qt_version)
            else:
                raise QtVersionError(
                    "The minimum supported Qt is version {} but you have "
                    "version {} installed. Please use 'sudo apt install qt5-default' upgrade Qt.".
                    format(Qt_version, version))
        util.check_openssl()

    def kill_port(self, port: str):
        cmd = "netstat -nlp | grep :%s| awk '{print $7}' | awk -F \"/\" '{ print $1 }'" % port
        status, output = subprocess.getstatusoutput(cmd)
        if status != 0 or output == '':
            return False
        logger.debug('kill_port output: %s' % output)
        pids = output.split('\n')
        if output.startswith("("):
            pids = pids[2:]
        elif output.startswith("（"):
            pids = pids[1:]
        if len(pids) == 0:
            return False
        for pid in pids:
            logger.debug('pid will kill: %s' % pid)
            try:
                if '/' in pid:
                    pid = pid.split('/')[0]
                if pid.isdigit():
                    if int(pid) != os.getpid():
                        os.kill(int(pid), signal.SIGKILL)
                        logger.info("kill port:%s pid:%s,parent process: %s" %
                                    (port, pid, os.getpid()))
                else:
                    raise OSError("error pid")
            except OSError:
                logger.info("failed kill port %s pid %s,process no exist" % (port, pid))
                logger.info(output)
        return True

    def kill_process(self, process_name):
        status, output = subprocess.getstatusoutput('pgrep %s' % process_name)
        if status != 0 or output == '':
            return
        pids = output.split('\n')
        for pid in pids:
            try:
                os.kill(int(pid), signal.SIGKILL.value)
                logger.debug("kill %s pid %s," % (process_name, pid))
            except OSError:
                logger.error("failed kill %s pid %s,process no exist" % (process_name, pid))

    def remove_state_file(self):
        data_path = PluginExeWorkPath + "data/data_*"
        if EnvConfig.situation <= 0:
            cmd = "rm -rf %s" % data_path
            os.system(cmd)

    def remove_log_file(self):
        log_path = PluginExeWorkPath + "log/Log_*"
        if EnvConfig.log_level <= 0:
            cmd = "rm -rf %s" % log_path
            os.system(cmd)

    def remove_tmpfile(self, filepath):
        cmd = "ls -l %s | grep '%s' | awk '{printf(\"%%s\\n\", $9)}'" % (filepath, PluginExeTmpFlag)
        status, output = subprocess.getstatusoutput(cmd)
        if status != 0 or output == '':
            return
        files = output.split('\n')
        for tmpfile in files:
            self.remove_file(filepath + tmpfile)

    def remove_file(self, filepath):
        if not os.path.exists(filepath):
            logger.debug("file %s not exist" % (filepath))
            return
        try:
            if not util.check_access(filepath):
                logger.error("{} no have {} Permission denied".format(util.get_username(),
                                                                      filepath))
            os.remove(filepath)
            logger.debug("remove %s sucess" % (filepath))
        except OSError:
            logger.error("remove %s failed" % (filepath))

    def set_radar_hx(self, radar_hx: RADAR_HX, blue=False, red=False):
        """[设置雷达]

        Arguments:
            radar_hx {RADAR_HX} -- [description]

        Keyword Arguments:
            blue {bool} -- [if True and red is False, set blue plane] (default: {False})
            red {bool} -- [description] (default: {False})

        Returns:
            [type] -- [set command status]
        """
        if red and not blue:
            cfg_flag = 1
        elif blue and not red:
            cfg_flag = 2
        else:
            return False
        cfg_path = PluginExeWorkPath + 'exe/platform' + str(
            cfg_flag) + '/config/plugin_config/radar_hx.json'
        return self._set_json_cfg(radar_hx, cfg_path)

    def set_iews_hx(self, iews_hx: IEWS_HX, blue=False, red=False):
        """[设置电子战]"""
        if red and not blue:
            cfg_flag = 1
        elif blue and not red:
            cfg_flag = 2
        else:
            return False
        cfg_path = PluginExeWorkPath + 'exe/platform' + str(
            cfg_flag) + '/config/plugin_config/iews_hx.json'
        return self._set_json_cfg(iews_hx, cfg_path)

    def _set_json_cfg(self, obj: object, cfg_path: str):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            text = f.read()
            obj_json = json.loads(text)
        ranges = getattr(obj, '_ranges_')
        for fieldname in ranges:
            min_r, max_r = ranges.get(fieldname)
            if hasattr(obj, fieldname):
                value = getattr(obj, fieldname)
                if min_r <= value <= max_r:
                    if fieldname in obj_json['config']:
                        obj_json['config'][fieldname] = value
                    else:
                        return False
                else:
                    return False
            else:
                return False
        with open(cfg_path, 'r+', encoding='utf-8') as f:
            text = json.dumps(obj_json, indent=4, separators=(',', ': '))
            f.write(text)
        return True


if __name__ == "__main__":
    plugin_exe = PluginExe()
    radar_hx = RADAR_HX()
    iews_hx = IEWS_HX()
    plugin_exe.set_radar_hx(radar_hx, blue=True)
    plugin_exe.set_iews_hx(iews_hx, blue=True)
