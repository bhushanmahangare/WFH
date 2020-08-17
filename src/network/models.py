from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# User Define packages
from authentication.models import AdmCustomer
from helper import enums


_macAddressValidator = RegexValidator("([A-Fa-f0-9]+[-:]){5}([A-Fa-f0-9])", "Invalid MAC address")

# Create your models here.
class Location( models.Model ):
    name = models.CharField(max_length=100, db_column='LocationName')
    customer = models.ForeignKey(
        AdmCustomer,
        db_column='CustomerId',
        db_constraint=False,
        on_delete=models.CASCADE
    )
    hotspotenable = models.BooleanField(db_column='HotspotEnable', blank=True, null=True)
    autologinenable = models.BooleanField(db_column='AutologinEnable', blank=True, null=True)
    automacregister = models.BooleanField(db_column='AutoMacRegister', blank=True, null=True)
    autologinvalidity = models.PositiveIntegerField(null=True, blank=True, db_column='AutoLoginValidity')
    autologinvalidity_unit = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(timeunit.value, timeunit.name) for timeunit in enums.TimeUnits], db_column='AutoLoginValidityUnit')
    interiminterval = models.PositiveSmallIntegerField(db_column='InterimInterval')

    class Meta:
        db_table = "location"


class APModel( models.Model ):
    displayname = models.CharField(max_length=60, db_column='DisplayName')
    apmodel = models.CharField(max_length=30, db_column='APModel')
    mac = models.CharField(max_length=100, db_column='Mac')
    apboardname = models.CharField(max_length=30, db_column='APBoardName')
    radio1 = models.BooleanField(null=True, blank=True, default=False, db_column='Radio1')
    radio2 = models.BooleanField(null=True, blank=True, default=False, db_column='Radio2')
    radio3 = models.BooleanField(null=True, blank=True, default=False, db_column='Radio3')
    maxssid = models.BooleanField(null=True, blank=True, default=False, db_column='MaxSSID')
    mutliwan = models.BooleanField(null=True, blank=True, default=False, db_column='MultiWAN')
    


class AP( models.Model ):
    apname = models.CharField(max_length=100, db_column='APName')
    macaddress = models.CharField(max_length=17, unique=True, validators=[_macAddressValidator], db_column='MacAddress')
    description = models.CharField(max_length=200, db_column='Description')
    apmodel = models.CharField(max_length=200, db_column='APModel')
    aptag = models.CharField(max_length=100, db_column='APTag')
    
    '''apconfigid = models.ForeignKey(
        Configuration
        db_column='configurationId',
        db_constraint=False
    )'''

    location = models.ForeignKey(
        Location,
        db_column='LocationId',
        db_constraint=False,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        AdmCustomer,
        db_column='CustomerId',
        db_constraint=False,
        on_delete=models.CASCADE
    )

    configchangedate = models.DateTimeField(null=True, blank=True, db_column='ConfigChangeDate')
    createdon = models.DateTimeField(auto_now_add=True, db_column='CreatedOn')
    modifiedon = models.DateTimeField(auto_now=True, db_column='ModifiedOn')    

    def save(self, *args, **kwargs):
        self.macaddress = self.macaddress.replace('-', ':').upper()
        return super(AP, self).save(*args, **kwargs)

    class Meta:
        db_table = "ap"


