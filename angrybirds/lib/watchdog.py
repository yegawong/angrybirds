#!/usr/bin/env python3
""" Watchdog class """
from threading import Timer
import logging

logger = logging.getLogger(__name__)


class Watchdog:

    def __init__(self, timeout, userHandler, name):  # timeout in seconds
        logger.debug("Initializing %s", self.__class__.__name__)
        self.isrunning = False
        self.timeout = timeout
        self.handler = userHandler
        self.timer = None
        self.name = name
        logger.debug("Initialized %s", self.__class__.__name__)

    def reset(self):
        self.stop()
        self.start()
        logger.debug("{} WatchDog reseted".format(self.name))

    def start(self):
        if not self.isrunning:
            self.timer = Timer(self.timeout, self.handler)
            self.timer.start()
            self.isrunning = True
        logger.debug("{} WatchDog started".format(self.name))

    def stop(self):
        if self.isrunning:
            self.timer.cancel()
            self.isrunning = False
        logger.debug("{} WatchDog stoped".format(self.name))
