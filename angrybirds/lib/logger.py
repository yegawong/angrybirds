#!/usr/bin/python
""" Logging Setup """
import collections
import logging
import os
import sys
import traceback
from angrybirds.lib.sysinfo import sysinfo
from datetime import datetime
from angrybirds.config import flag_log_setup
CRITICAL = 'CRITICAL'
FATAL = 'CRITICAL'
ERROR = 'ERROR'
WARNING = 'WARNING'
WARN = 'WARNING'
INFO = 'INFO'
DEBUG = 'DEBUG'
NOTSET = 'NOTSET'


class BridLoggerFormatter(logging.Formatter):
    """ Override formatter to strip newlines the final message """

    def format(self, record):
        record.message = record.getMessage()
        # strip newlines
        if "\n" in record.message or "\r" in record.message:
            record.message = record.message.replace("\n", "\\n").replace("\r", "\\r")

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        msg = self.formatMessage(record)
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if msg[-1:] != "\n":
                msg = msg + "\n"
            msg = msg + record.exc_text
        if record.stack_info:
            if msg[-1:] != "\n":
                msg = msg + "\n"
            msg = msg + self.formatStack(record.stack_info)
        return msg


class RollingBuffer(collections.deque):
    """File-like that keeps a certain number of lines of text in memory."""

    def write(self, buffer):
        """ Write line to buffer """
        for line in buffer.rstrip().splitlines():
            self.append(line + "\n")


def set_root_logger(loglevel=logging.INFO):
    """ Setup the root logger. """
    rootlogger = logging.getLogger()
    rootlogger.setLevel(loglevel)
    return rootlogger


def log_setup(loglevel):
    """ initial log set up. """
    global flag_log_setup
    if flag_log_setup:
        return
    flag_log_setup = True
    numeric_loglevel = get_loglevel(loglevel)
    root_loglevel = min(logging.DEBUG, numeric_loglevel)
    rootlogger = set_root_logger(loglevel=root_loglevel)
    log_format = BridLoggerFormatter(
        "%(asctime)s %(processName)-15s %(threadName)-15s "
        "%(module)-15s %(funcName)-25s %(levelname)-8s %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S")
    s_handler = stream_handler(numeric_loglevel)
    c_handler = crash_handler(log_format)
    rootlogger.addHandler(s_handler)
    rootlogger.addHandler(c_handler)
    logging.info("Log level set to: %s", loglevel.upper())


def stream_handler(loglevel):
    """ Add a logging cli handler """
    # Don't set stdout to lower than verbose
    loglevel = max(loglevel, 10)
    log_format = BridLoggerFormatter("%(asctime)s %(levelname)-8s %(message)s",
                                     datefmt="%m/%d/%Y %H:%M:%S")
    log_console = logging.StreamHandler(sys.stdout)
    log_console.setFormatter(log_format)
    log_console.setLevel(loglevel)
    return log_console


def crash_handler(log_format):
    """ Add a handler that sores the last 100 debug lines to 'debug_buffer'
        for use in crash reports """
    log_crash = logging.StreamHandler(debug_buffer)
    log_crash.setFormatter(log_format)
    log_crash.setLevel(logging.DEBUG)
    return log_crash


def get_loglevel(loglevel):
    """ Check valid log level supplied and return numeric log level """
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)

    return numeric_level


def crash_log():
    """ Write debug_buffer to a crash log on crash """

    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    filename = os.path.join(path, datetime.now().strftime("crash_report.%Y.%m.%d.%H%M%S%f.log"))

    freeze_log = list(debug_buffer)
    # with open(filename, "w") as outfile:
    #     outfile.writelines(freeze_log)
    #     traceback.print_exc(file=outfile)
    #     outfile.write(sysinfo)
    for log in freeze_log:
        print(log, end='')  # not save log file
    return filename


# Stores the last 100 debug messages
debug_buffer = RollingBuffer(maxlen=100)  # pylint: disable=invalid-name
