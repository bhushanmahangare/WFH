from enum import IntEnum, Enum

class AutoLoginTypes(Enum):
    USER = 'USER DEVICE'
    DEVICE = 'NON BROWSER DEVICE'

class UserStatus(Enum):
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'
    SUSPENDED = 'SUSPENDED'
    PENDING = 'PENDING'
    DENIED = 'DENIED'

class TimeUnits(IntEnum):
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4
    WEEK = 5

class BandwidthUnits(IntEnum):
    KB = 1
    MB = 2
    GB = 3

class BandwidthRateUnits(IntEnum):
    Kbps = 1
    Mbps = 2
    Gbps = 3