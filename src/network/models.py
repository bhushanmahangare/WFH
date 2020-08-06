from django.db import models

# User Define packages
from authentication.models import AdmCustomer
from helper import enums


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