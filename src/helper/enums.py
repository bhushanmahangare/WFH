from enum import IntEnum, Enum

'''
@param 
@author Bhushan Mahangare
@return return Enum class
@description Enum declartions
'''

class CustomerTypes(Enum):
        ''' Super admin 1 
            Account admin 2
            Manger admin 3
            subscriber   4'''
        SUPERADMIN = 1              # This user like Superadmin in wifilan 
        ITADMIN = 2                 # This user like customers in wifilan Or Account admin
        MANAGER = 3                 # This user like resellers in wifilan
        SUBSCRIBER = 4              # This is new login method to end customer who used WFH solutions

class TimeUnits(IntEnum):
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4
    WEEK = 5