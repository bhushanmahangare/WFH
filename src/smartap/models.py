from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# User Define packages
from authentication.models import AdmCustomer
from helper import enums

_macAddressValidator = RegexValidator("([A-Fa-f0-9]+[-:]){5}([A-Fa-f0-9])", "Invalid MAC address")

class AP( models.Model ):
    
    macaddress = models.CharField(max_length=17, unique=True, validators=[_macAddressValidator], db_column='MacAddress')
    lastcheckintime = models.DateTimeField(null=True, blank=True, db_column='LastCheckinTime')
    laststatusid = models.IntegerField(blank=True, null=True, db_column='LastStatusId')
    sshpassword = models.CharField(max_length=100,blank=True , null=True, default='lkpewrtyu@', db_column='SSHPassword')
    adminpassword = models.CharField(max_length=100,blank=True , null=True, default='qw4rk6ba23', db_column='AdminPassword')
    configchangedate = models.DateTimeField(null=True, blank=True, db_column='ConfigChangeDate')
    fastcheckin = models.BooleanField(null=True, blank=True, default=0, db_column='FastCheckin')
    reboot = models.BooleanField(null=True, blank=True, default=0, db_column='Reboot')
    speedtest = models.BooleanField(null=True, blank=True, default=0, db_column='SpeedTest')
    
    radio1channel = models.BooleanField(null=True, blank=True, default=0, db_column='Radio1Channel')
    radio2channel = models.BooleanField(null=True, blank=True, default=0, db_column='Radio2Channel')
    radio3channel = models.BooleanField(null=True, blank=True, default=0, db_column='Radio3Channel')
    radio1channelwidth = models.SmallIntegerField(null=True, blank=True, default=20, db_column='Radio1ChannelWidth')
    radio2channelwidth = models.SmallIntegerField(null=True, blank=True, default=20, db_column='Radio2ChannelWidth')
    radio3channelwidth = models.SmallIntegerField(null=True, blank=True, default=20, db_column='Radio3ChannelWidth')
    radio1Power = models.CharField(max_length=10,blank=True , null=True, default='0', db_column='Radio1Power')
    radio2Power = models.CharField(max_length=10,blank=True , null=True, default='0', db_column='Radio2Power')
    radio3Power = models.CharField(max_length=10,blank=True , null=True, default='0', db_column='Radio3Power')

    isgpsenabled = models.BooleanField(null=True, blank=True, default=0, db_column='IsGpsEnabled')
    gpslat = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='GpsLat')
    gpslong = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='GpsLong')
    gpsupdatetime = models.DateTimeField(null=True, blank=True, db_column='GpsUpdateTime')

    publicipaddress = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True, db_column='PublicIpAddress')
    wanipaddress = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True, db_column='WanIpAddress')

    commandexec = models.BooleanField(null=True, blank=True, default=0, db_column='CommandExec')
    apuptime = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='ApUptime')

    firmwareupgrade = models.BooleanField(null=True, blank=True, default=0, db_column='FirmwareUpgrade')
    firmwareversion = models.CharField(max_length=40,blank=True , null=True, default='0', db_column='FirmwareVersion')
    upgradeconfigbackup = models.BooleanField(null=True, blank=True, default=0, db_column='UpgradeConfigBackup')
    currentfirmwareversion = models.CharField(max_length=40,blank=True , null=True, default='0', db_column='CurrentFirmwareVersion')
    firmwareupgradeschedule = models.BooleanField(null=True, blank=True, default=0, db_column='FirmwareUpgradeSchedule')
    firmwareupgradescheduledatetime = models.CharField(max_length=40,blank=True , null=True, default='0', db_column='FirmwareUpgradeScheduleDateTime')
    apboardname = models.CharField(max_length=40,blank=True , null=True, default='0', db_column='ApBoardName')

    multiwanmode = models.BooleanField(null=True, blank=True, default=0, db_column='MultiWanMode')
    wanlinks = models.CharField(max_length=20,blank=True , null=True, default='Wired:Up', db_column='WanLinks')
    wanspeeddownlink = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='WanSpeedDownlink')
    wanspeeduplink = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='WanSpeedUplink')
    
    wirelessclients = models.SmallIntegerField(null=True, blank=True, default=0, db_column='WirelessClients')
    wiredclients = models.SmallIntegerField(null=True, blank=True, default=0, db_column='WiredClients')
    hotspottotalclientcount = models.SmallIntegerField(null=True, blank=True, default=0, db_column='HotspotTotalClientCount')
    hotspotauthenticatedclientcount = models.SmallIntegerField(null=True, blank=True, default=0, db_column='HotspotAuthenticatedClientCount')
    
    rsyslogenable = models.BooleanField(null=True, blank=True, default=0, db_column='RSysLogEnable')
    rsyslogserver = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='RSysLogServer')
    rsyslogport = models.CharField(max_length=20,blank=True , null=True, default='514', db_column='RSysLogPort')
    rsyslogprefix = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='RSysLogDuration')
    rsyslogduration = models.CharField(max_length=20,blank=True , null=True, default='0', db_column='RSysLogPrefix')
    rsyslogdate = models.DateTimeField(null=True, blank=True, db_column='RSysLogDate')

    wifilanserverid = models.IntegerField(db_column='WifilanServerId')
    wifilancustomerid = models.IntegerField(db_column='WifilanCustomerId')
    wifilanoperatorid = models.IntegerField(blank=True, null=True, db_column='WifilanOperatorId')
    wifilanlocationid = models.IntegerField(db_column='WifilanLocationId')
    wifilanapid = models.IntegerField(null=False, blank=False, db_column='WifilanAPId')

    createdon = models.DateTimeField(auto_now_add=True, db_column='CreatedOn')
    modifiedon = models.DateTimeField(auto_now=True, db_column='ModifiedOn')
    
    def save(self, *args, **kwargs):
        self.macaddress = self.macaddress.replace('-', ':').upper()
        return super(AP, self).save(*args, **kwargs)

    class Meta:
        # app_label helps django to recognize your db
        app_label = 'smartap'
        db_table = "ap"