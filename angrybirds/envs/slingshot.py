#!/usr/bin/python
""" Slingshot Env Class """
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
import os
import sys
import threading

from twisted.internet.endpoints import TCP4ServerEndpoint
from angrybirds.lib.logger import crash_log, log_setup
from angrybirds.lib.watchdog import Watchdog
from angrybirds.plugins.net.client import ControllerClientFactory
from angrybirds.plugins.net.server import DataInterfaceFactory
from angrybirds.plugins.convert.controller import Controller
from angrybirds.config.plane_config import CommunicationPort, EnvConfig
from angrybirds.plugins.game.plugin_exe import PluginExe
from angrybirds.plugins.convert.plane import BridCoder
from angrybirds.config.sim_env_config import PluginExeTimeout, PluginExeControlTimeout
from angrybirds.plugins.game.auth_sever import AuthServerFactory

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Slingshot(gym.Env):
    """
    Description:
        I'm one of the angrybirds env, I need the action of red planes and blue planes and
        fixed rules to fight against opponents. I will return to the status of the two planes
        in the simulation.

    Source:
        This environment corresponds to the version of the angrybirds problem described by self and
        fixed rules opponents.

    Observation:
        Type: Box(...)
        Num	Observation                    Min        Max
        0   AIData.AATargetDataListNum       0         20
        ...

    Actions:
        Type: Discrete(40)
        Num	Action
        0	AIInputData
        ...

    Reward:
        Reward is constants.Reward for every step taken, including the termination step

    Starting State:
        All aircraft observations are configured by args.

    Episode Termination:
        done is True Time, AIData.sOtherInfo will give the reason for the termination.
    """

    def __init__(self, log_level='ERROR'):
        log_setup(log_level)
        logger.debug("Executing: %s. PID: %s", self.__class__.__name__, os.getpid())
        logger.debug("Initializing %s", self.__class__.__name__)
        # This keeps track of how many steps the environment is running.
        self.step_num = 0
        self.exe_status = 'IDIE'
        self._closed = False
        self._old_obs = None
        self._old_action = None
        self._is_crash = False
        # Observation and Action Spaces. These are both geared towards a single
        # agent even though the environment expects actions and returns
        # observations for all four agents. We do this so that it's clear what
        # the actions and obs are for a single agent. Wrt the observations,
        # they are actually returned as a dict for easier understanding.
        self._set_action_space()
        self._set_observation_space()
        try:
            self.coder = BridCoder()
            self.pluginexe = PluginExe()
            self._init_communication_port()
            self.pluginexe.stop_exe()
            self.pluginexe.start_exe()
            self.watchdog = Watchdog(timeout=PluginExeTimeout, userHandler=self._Handle, name='Slingshot')
        except Exception:
            self._is_crash = True
            crash_file = crash_log()
            logger.exception("Got Exception on Slingshot handler:")
            logger.critical(
                "An unexpected crash has occurred. Crash report written to '%s'. "
                "You MUST provide this file if seeking assistance. Please verify you "
                "are running the latest version of angrybirds before reporting", crash_file)
        logger.info("reactor status running")
        logger.debug("Initialized %s", self.__class__.__name__)

    def _init_communication_port(self):
        if 'twisted.internet.reactor' in sys.modules:
            del sys.modules['twisted.internet.reactor']
        from twisted.internet import default
        default.install()
        from twisted.internet import reactor
        self.dataer = DataInterfaceFactory(client_cnt=EnvConfig.plane_count)
        controller_endpoint = ControllerClientFactory()
        self.controller = Controller(controller_endpoint)
        self.dataer_port = reactor.listenTCP(CommunicationPort.data,
                                             self.dataer,
                                             interface=CommunicationPort.host)
        self.auth_server = AuthServerFactory()
        self.auth_server_port = reactor.listenTCP(55555,
                                                  self.auth_server,
                                                  interface=CommunicationPort.host)
        reactor.connectTCP(CommunicationPort.host, CommunicationPort.control, controller_endpoint)
        self.mthread = threading.Thread(target=reactor.run, args=(False,))
        self.mthread.setDaemon(True)
        self.mthread.start()

    def _set_action_space(self):
        pass

    def _set_observation_space(self):
        """The Observation Space for each agent"""
        pass

    def _Handle(self):
        """[envirment reset]

        Returns:
            [tuple] -- [observations]
        """
        logger.debug("[ENV HANDLE]")
        logger.error("Got Exception on Slingshot handler: Algorithm processing timeout")
        self.watchdog.stop()
        self.exe_status == 'TIMEOUT'
        self.controller.stop()

    def reset(self):
        """[envirment reset]

        Returns:
            [tuple] -- [observations]
        """
        logger.debug("[ENV RESET]")
        self.step_num = 0
        try:
            if self._is_crash:
                return [], None, True, {'crash': True}
            return self.__reset()
        except Exception:
            if self._is_crash:
                return [], None, True, {'crash': True}
            self._is_crash = True
            crash_file = crash_log()
            logger.exception("Got Exception on Slingshot handler:")
            logger.critical(
                "An unexpected crash has occurred. Crash report written to '%s'. "
                "You MUST provide this file if seeking assistance. Please verify you "
                "are running the latest version of angrybirds before reporting", crash_file)
            return [], None, True, {'crash': True}

    def step(self, actions: list):
        """[envirment step]

        Arguments:
            actions {[list]} -- [AIinputData]

        Returns:
            [object] -- [AIData]
        """
        self.step_num += 1
        logger.debug("[ENV STEP]")
        try:
            if self._is_crash:
                return [], None, True, {'crash': True}
            return self.__step(actions)
        except Exception:
            if self._is_crash:
                return [], None, True, {'crash': True}
            self._is_crash = True
            crash_file = crash_log()
            logger.exception("Got Exception on Slingshot handler:")
            logger.critical(
                "An unexpected crash has occurred. Crash report written to '%s'. "
                "You MUST provide this file if seeking assistance. Please verify you "
                "are running the latest version of angrybirds before reporting", crash_file)
            return [], None, True, {'crash': True}

    def get_old_action(self):
        return self._old_action

    def __reset(self):
        """[envirment reset]

        Returns:
            [list] -- [AIData]
        """
        self.watchdog.stop()
        obs, rew, done, info = [], None, False, {'crash': False}
        if self.exe_status == 'IDIE':
            self.controller.scenario()
            self.controller.init()
            self.controller.start()
            self.exe_status = 'START'
        elif self.exe_status == 'START':
            self.controller.stop()
            self.controller.scenario()
            self.controller.init()
            self.controller.start()
            self.exe_status = 'START'
        elif self.exe_status == 'PAUSE':
            self.controller.start()
            self.exe_status = 'START'
        elif self.exe_status == 'STOP':
            self.controller.scenario()
            self.controller.init()
            self.controller.start()
            self.exe_status = 'START'
        elif self.exe_status == 'TIMEOUT' or self.exe_status == 'WAITRESET':
            self.controller.stop()
            self.controller.scenario()
            self.controller.init()
            self.controller.start()
            self.exe_status = 'START'
        data_list = self.dataer.initData()
        self.watchdog.reset()
        if self._old_action is None:
            self._old_action = [self.coder.generate_aiiputdata()] * EnvConfig.plane_count
        obs = self._decode(data_list)
        return obs, rew, done, info

    def __step(self, actions):
        obs, rew, done, info = [], None, False, {'crash': False}
        self._old_action = actions
        if self.exe_status == 'IDIE':
            self.watchdog.stop()
            return self.reset()
        elif self.exe_status == 'PAUSE':
            self.controller.start()
            self.exe_status = 'START'
            data_list = self.dataer.initData()
        elif self.exe_status == 'STOP':
            self.watchdog.stop()
            done = True
            return self._old_obs, rew, done, info
        elif self.exe_status == 'TIMEOUT':
            self.watchdog.stop()
            done = True
            info['crash'] = True
            return self._old_obs, rew, done, info
        elif self.exe_status == 'WAITRESET':
            self.watchdog.stop()
            done = True
            return self._old_obs, rew, done, info
        self.watchdog.stop()
        send_action = []
        for action in actions:
            send_action.append(self.coder.encode_aiiputdata(action))
        data_list = self.dataer.sendAll(send_action, timeout=PluginExeControlTimeout)
        self.watchdog.reset()   # start check if the algorithm times out
        obs = self._decode(data_list)
        self._old_obs = obs
        for ob in obs:
            if ob.sOtherInfo.bOver is True:
                logger.debug('[ENV DONE]')
                done = True
                self.watchdog.stop()
                self.exe_status = 'WAITRESET'
                break
        return obs, rew, done, info

    def _decode(self, data_list: list):
        obs = []
        for data in data_list:
            obs.append(self.coder.decode_aidata(data))
        return obs

    def render(self):
        pass

    def seed(self, seed=None):
        pass

    def close(self):
        self._closed = True
        from twisted.internet import reactor
        if hasattr(self, 'dataer_port'):
            self.dataer_port.loseConnection()
            self.dataer_port.connectionLost(reason="Slingshot Close")
        if hasattr(self, 'auth_server_port'):
            self.auth_server_port.loseConnection()
            self.auth_server_port.connectionLost(reason="Slingshot Close")
        reactor.crash()
        logger.debug("[ENV CLOSE]")
        if hasattr(self, 'watchdog'):
            self.watchdog.stop()
        if hasattr(self, 'pluginexe'):
            self.pluginexe.stop_exe()

    def __del__(self):
        if not self._closed:
            self.close()
