from enum import IntEnum, Enum

'''
@param 
@author Bhushan Mahangare
@return return Enum class
@description Enum declartions
'''
class CustomerTypes(Enum):
    SUPERADMIN = 'SUPER ADMIN' # This user like Superadmin in wifilan 
    ITADMIN = 'IT ADMIN'       # This user like customers in wifilan
    MANAGER = 'MANAGER'         # This user like resellers in wifilan
    SUBSCRIBER = 'SUBSCRIBER'   # This is new login method to end customer who used WFH solutions