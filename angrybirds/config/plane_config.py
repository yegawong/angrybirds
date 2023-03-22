#!/usr/bin/env python3
""" Parent class for mask adjustments for plan converter """
import logging
from enum import Enum
logger = logging.getLogger(__name__)


class EnvConfig:
    _fields_ = [
        ('B', 'beat'),
        ('B', 'record'),
        ('B', 'situation'),
        ('B', 'log'),
        ('B', 'cloud'),
        ('B', 'rain'),
        ('B', 'fog'),
        ('B', 'plane_count'),
    ]
    beat = 1  # 应该取红蓝机最大公约数
    record = 0  # 回放数据
    situation = 0  # 态势数据
    log = 0  # 日志数据
    cloud = 0
    rain = 0
    fog = 0
    plane_count = 2
    log_level = -1
    red_beat = 1
    blue_beat = 20


class CombatZoneConfig:
    # Origin of coordinates is 115 longitude 30 latitude
    longitude = 115
    latitude = 30


class PlaneConfig:
    _fields_ = [
        ('d', 'longitude'),
        ('d', 'latitude'),
        ('d', 'height'),
        ('d', 'heading'),
        ('d', 'speed'),
        ('d', 'fuel'),
    ]
    _ranges_ = {
        'longitude': (114.4, 115.6),
        'latitude': (29.8, 31.8),
        'height': (0.0, 10000.0),
        'heading': (-180.0, 180.0),
        'speed': (0.6, 1.0),
        'fuel': (2000.0, 3000.0),
    }


class RedPlane(PlaneConfig):
    longitude = 115.0
    latitude = 30.4
    height = 6000.0
    heading = 0.0
    speed = 240.0
    fuel = 3000.0


class BluePlane(PlaneConfig):
    longitude = 115.0
    latitude = 30.6
    height = 6000.0
    heading = 180.0
    speed = 240.0
    fuel = 3000.0


class RequestMsgID(Enum):
    SCENARIO = 0
    INIT = 2
    START = 4
    PAUSE = 6
    STOP = 10


class ResponseMsgID(Enum):
    SCENARIO = 1
    INIT = 3
    START = 5
    PAUSE = 7
    STOP = 11


class ResponseMsgCode:
    Code = {
        0: "IDIE",
        1: "想定",
        2: "初始化",
        3: "运行",
        4: "暂停",
        9: "正常",
    }


class CommunicationPort:
    control = 60000
    data = 60001
    host = '127.0.0.1'


class IEWS_HX:
    _ranges_ = {
        'EW_performs': (1.2, 1.32),
        # Constant value without random
        'active_alarm_distance': (0.0, 0.0),
        'passive_alarm_distance': (0.0, 0.0),
        'Deceptive_v': (90.0, 110.0),
        'Deceptive_d': (18.0, 22.0),
        'Deceptive_s': (450000.0, 500000.0),
        'Deceptive_s_lim': (27000.0, 33000.0),
    }

    EW_performs = 1.2
    active_alarm_distance = 0.0
    passive_alarm_distance = 0.0
    Deceptive_v = 100.0
    Deceptive_d = 20.0
    Deceptive_s = 500000.0
    Deceptive_s_lim = 30000.0


class RADAR_HX:
    _ranges_ = {
        'm_fBeamWidth': (2.5, 2.75),
        'm_fFreq': (9, 11),
        # Constant value without random
        'm_nPolaMode': (0, 1),
        'm_fPower': (1600.0, 1760.0),
        'm_fScanLimitAz': (60.0, 60.0),
        'm_fScanLimitEl': (60.0, 60.0),
        'm_fGainAntenna_dB': (33.0, 35.0),
    }

    m_fBeamWidth = 2.5
    m_fFreq = 10.0
    m_nPolaMode = 0
    m_fPower = 1600.0
    m_fScanLimitAz = 60.0
    m_fScanLimitEl = 30.0
    m_fGainAntenna_dB = 34.0
