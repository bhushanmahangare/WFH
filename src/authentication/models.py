from django.db import models                            # DB datatypes
#from django.contrib.auth.models import AbstractUser     # Used Django User auth

#from django.core.validators import RegexValidator       #Validation package
#from django.core.exceptions import ValidationError      #Validation exception package
#from django.utils import timezone                       #Timezone package UTC
#import random
#import ipaddress
#import string
#import pytz             #Timezone DB
#import datetime

# Custome packages import
#from Helper import *

#_macAddressValidator = RegexValidator("([A-Fa-f0-9]+[-:]){5}([A-Fa-f0-9])", "Invalid MAC address")


#class AuthUsers(AbstractUser):
class Data(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_login = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.username