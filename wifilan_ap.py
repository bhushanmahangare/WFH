# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ApModels(models.Model):
    displayname = models.CharField(db_column='DisplayName', max_length=60)  # Field name made lowercase.
    apmodel = models.CharField(db_column='APModel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apboardname = models.CharField(db_column='ApBoardName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radio1 = models.IntegerField(db_column='Radio1', blank=True, null=True)  # Field name made lowercase.
    radio2 = models.IntegerField(db_column='Radio2', blank=True, null=True)  # Field name made lowercase.
    radio3 = models.IntegerField(db_column='Radio3', blank=True, null=True)  # Field name made lowercase.
    maxssid = models.IntegerField(db_column='MaxSSID', blank=True, null=True)  # Field name made lowercase.
    multiwan = models.IntegerField(db_column='MultiWAN', blank=True, null=True)  # Field name made lowercase.
    number_3g = models.IntegerField(db_column='3G', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4g = models.IntegerField(db_column='4G', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    webfiltering = models.IntegerField(db_column='WebFiltering', blank=True, null=True)  # Field name made lowercase.
    presence = models.IntegerField(db_column='Presence', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_models'



class Ap(models.Model):
    apname = models.CharField(db_column='ApName', max_length=40)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', unique=True, max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    apmodel = models.CharField(db_column='APModel', max_length=30)  # Field name made lowercase.
    aptag = models.CharField(db_column='APTag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aptemplateid = models.IntegerField(db_column='ApTemplateId')  # Field name made lowercase.
    wlanprofileid = models.IntegerField(db_column='WLanProfileId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    configchangedate = models.DateTimeField(db_column='ConfigChangeDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap'

class ApMacPoliciesDevicelist(models.Model):
    macaddress = models.CharField(db_column='MacAddress', max_length=17, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    policyid = models.ForeignKey('ApMacPolicyProfile', models.DO_NOTHING, db_column='PolicyId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    lastmodifiedtime = models.DateTimeField(db_column='LastModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_mac_policies_devicelist'


class ApMacPolicyProfile(models.Model):
    profilename = models.CharField(db_column='ProfileName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    actiontype = models.CharField(db_column='ActionType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    lastmodifiedtime = models.DateTimeField(db_column='LastModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_mac_policy_profile'


class ApMobilityDomain(models.Model):
    mobilitydomainname = models.CharField(db_column='MobilityDomainName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_mobility_domain'


class ApProfiles(models.Model):
    profilename = models.CharField(db_column='ProfileName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    devicetypeid = models.PositiveIntegerField(db_column='DeviceTypeId', blank=True, null=True)  # Field name made lowercase.
    enablemultiwan = models.IntegerField(db_column='EnableMultiWan', blank=True, null=True)  # Field name made lowercase.
    multiwanmethod = models.CharField(db_column='MultiwanMethod', max_length=13, blank=True, null=True)  # Field name made lowercase.
    primaryload = models.IntegerField(db_column='PrimaryLoad', blank=True, null=True)  # Field name made lowercase.
    secondaryload = models.IntegerField(db_column='SecondaryLoad', blank=True, null=True)  # Field name made lowercase.
    tertinaryload = models.IntegerField(db_column='TertinaryLoad', blank=True, null=True)  # Field name made lowercase.
    quadrilateralload = models.IntegerField(db_column='QuadrilateralLoad', blank=True, null=True)  # Field name made lowercase.
    overridehotspotenable = models.IntegerField(db_column='OverrideHotspotEnable', blank=True, null=True)  # Field name made lowercase.
    hotspotplan = models.IntegerField(db_column='HotspotPlan', blank=True, null=True)  # Field name made lowercase.
    radiusserver1 = models.CharField(db_column='RadiusServer1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radiusserver2 = models.CharField(db_column='RadiusServer2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radiussecret = models.CharField(db_column='RadiusSecret', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radiusnasid = models.CharField(db_column='RadiusNasId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uamserver = models.CharField(db_column='UamServer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passthroughurl = models.CharField(db_column='PassthroughUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    macpassword = models.CharField(db_column='MacPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    autologinenable = models.IntegerField(db_column='AutologinEnable', blank=True, null=True)  # Field name made lowercase.
    autologinvalidity = models.IntegerField(db_column='AutoLoginValidity', blank=True, null=True)  # Field name made lowercase.
    autologinvalidityunit = models.IntegerField(db_column='AutoLoginValidityUnit', blank=True, null=True)  # Field name made lowercase.
    automacenable = models.IntegerField(db_column='AutoMacEnable', blank=True, null=True)  # Field name made lowercase.
    hotspotipaddress = models.CharField(db_column='HotspotIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    interiminterval = models.IntegerField(db_column='InterimInterval', blank=True, null=True)  # Field name made lowercase.
    radiocountrycode = models.CharField(db_column='RadioCountryCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    radio12400enable = models.IntegerField(db_column='Radio12400Enable', blank=True, null=True)  # Field name made lowercase.
    radio12400channel = models.IntegerField(db_column='Radio12400Channel', blank=True, null=True)  # Field name made lowercase.
    radio12400txpower = models.IntegerField(db_column='Radio12400TxPower', blank=True, null=True)  # Field name made lowercase.
    radio12400bandwidth = models.IntegerField(db_column='Radio12400Bandwidth', blank=True, null=True)  # Field name made lowercase.
    radio12400backgrounscan = models.IntegerField(db_column='Radio12400BackgrounScan', blank=True, null=True)  # Field name made lowercase.
    radio12400scantime = models.IntegerField(db_column='Radio12400ScanTime', blank=True, null=True)  # Field name made lowercase.
    radio12400maxclients = models.IntegerField(db_column='Radio12400MaxClients', blank=True, null=True)  # Field name made lowercase.
    radio25000enable = models.IntegerField(db_column='Radio25000Enable', blank=True, null=True)  # Field name made lowercase.
    radio25000channel = models.IntegerField(db_column='Radio25000Channel', blank=True, null=True)  # Field name made lowercase.
    radio25000txpower = models.IntegerField(db_column='Radio25000TxPower', blank=True, null=True)  # Field name made lowercase.
    radio25000bandwidth = models.IntegerField(db_column='Radio25000Bandwidth', blank=True, null=True)  # Field name made lowercase.
    radio25000backgrounscan = models.IntegerField(db_column='Radio25000BackgrounScan', blank=True, null=True)  # Field name made lowercase.
    radio25000scantime = models.IntegerField(db_column='Radio25000ScanTime', blank=True, null=True)  # Field name made lowercase.
    radio25000maxclients = models.IntegerField(db_column='Radio25000MaxClients', blank=True, null=True)  # Field name made lowercase.
    radio35000enable = models.IntegerField(db_column='Radio35000Enable', blank=True, null=True)  # Field name made lowercase.
    radio35000channel = models.IntegerField(db_column='Radio35000Channel', blank=True, null=True)  # Field name made lowercase.
    radio35000txpower = models.IntegerField(db_column='Radio35000TxPower', blank=True, null=True)  # Field name made lowercase.
    radio35000bandwidth = models.IntegerField(db_column='Radio35000Bandwidth', blank=True, null=True)  # Field name made lowercase.
    radio35000backgrounscan = models.IntegerField(db_column='Radio35000BackgrounScan', blank=True, null=True)  # Field name made lowercase.
    radio35000maxclients = models.IntegerField(db_column='Radio35000MaxClients', blank=True, null=True)  # Field name made lowercase.
    radio35000scantime = models.IntegerField(db_column='Radio35000ScanTime', blank=True, null=True)  # Field name made lowercase.
    configchangedate = models.DateTimeField(db_column='ConfigChangeDate', blank=True, null=True)  # Field name made lowercase.
    customdnsenable = models.PositiveIntegerField(db_column='CustomDNSEnable', blank=True, null=True)  # Field name made lowercase.
    primarydns = models.CharField(db_column='PrimaryDNS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarydns = models.CharField(db_column='SecondaryDNS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    presenceanalyticsenable = models.PositiveIntegerField(db_column='PresenceAnalyticsEnable', blank=True, null=True)  # Field name made lowercase.
    rfcutoffthreshold = models.IntegerField(db_column='RfCutoffThreshold', blank=True, null=True)  # Field name made lowercase.
    datauploadinterval = models.IntegerField(db_column='DataUploadInterval', blank=True, null=True)  # Field name made lowercase.
    dataformat = models.CharField(db_column='DataFormat', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dataserver = models.CharField(db_column='DataServer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dataserverauthkey = models.CharField(db_column='DataServerAuthKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lanportmode = models.CharField(db_column='LanPortMode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enablemanagementframeprotection = models.PositiveIntegerField(db_column='EnableManagementFrameProtection', blank=True, null=True)  # Field name made lowercase.
    enabledfs = models.PositiveIntegerField(db_column='EnableDFS', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_profiles'


class ApRadiusProfile(models.Model):
    profilename = models.CharField(db_column='ProfileName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dedicatedauthandacceserver = models.IntegerField(db_column='DedicatedAuthAndAcceServer')  # Field name made lowercase.
    primaryauthenticationserver = models.CharField(db_column='PrimaryAuthenticationServer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    primaryauthenticationserverport = models.IntegerField(db_column='PrimaryAuthenticationServerPort', blank=True, null=True)  # Field name made lowercase.
    primaryauthenticationserversecret = models.CharField(db_column='PrimaryAuthenticationServerSecret', max_length=15, blank=True, null=True)  # Field name made lowercase.
    primaryaccountingserver = models.CharField(db_column='PrimaryAccountingServer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    primaryaccountingserverport = models.IntegerField(db_column='PrimaryAccountingServerPort', blank=True, null=True)  # Field name made lowercase.
    primaryaccountingserversecret = models.CharField(db_column='PrimaryAccountingServerSecret', max_length=15, blank=True, null=True)  # Field name made lowercase.
    enableradiusfailover = models.IntegerField(db_column='EnableRadiusFailover')  # Field name made lowercase.
    secondaryauthenticationserver = models.CharField(db_column='SecondaryAuthenticationServer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondaryauthenticationserverport = models.IntegerField(db_column='SecondaryAuthenticationServerPort', blank=True, null=True)  # Field name made lowercase.
    secondaryauthenticationserversecret = models.CharField(db_column='SecondaryAuthenticationServerSecret', max_length=15, blank=True, null=True)  # Field name made lowercase.
    secondaryradiusaccountingserver = models.CharField(db_column='SecondaryRadiusAccountingServer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondaryradiusaccountingport = models.IntegerField(db_column='SecondaryRadiusAccountingPort', blank=True, null=True)  # Field name made lowercase.
    secondaryradiusaccountingsecret = models.CharField(db_column='SecondaryRadiusAccountingSecret', max_length=15, blank=True, null=True)  # Field name made lowercase.
    radiusretryprimaryinterval = models.IntegerField(db_column='RadiusRetryPrimaryInterval', blank=True, null=True)  # Field name made lowercase.
    interimaccountingupdateinterval = models.IntegerField(db_column='InterimAccountingUpdateInterval', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_radius_profile'


class ApSdwan(models.Model):
    sdwanprofilename = models.CharField(db_column='SDWanProfileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdwanprofilenameauto = models.CharField(db_column='SDWanProfileNameAuto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdwantype = models.IntegerField(db_column='SDWanType', blank=True, null=True)  # Field name made lowercase.
    sdwantrafficflowtype = models.IntegerField(db_column='SDWanTrafficFlowType', blank=True, null=True)  # Field name made lowercase.
    sdwanvlanenable = models.PositiveIntegerField(db_column='SDWanVlanEnable', blank=True, null=True)  # Field name made lowercase.
    sdwanvlanid = models.PositiveIntegerField(db_column='SDWanVlanId', blank=True, null=True)  # Field name made lowercase.
    sdwanvpncertificate = models.TextField(db_column='SDWanVPNCertificate', blank=True, null=True)  # Field name made lowercase.
    enablemultiwan = models.IntegerField(db_column='EnableMultiWan', blank=True, null=True)  # Field name made lowercase.
    multiwanmethod = models.CharField(db_column='MultiwanMethod', max_length=13, blank=True, null=True)  # Field name made lowercase.
    primaryload = models.IntegerField(db_column='PrimaryLoad', blank=True, null=True)  # Field name made lowercase.
    secondaryload = models.IntegerField(db_column='SecondaryLoad', blank=True, null=True)  # Field name made lowercase.
    tertinaryload = models.IntegerField(db_column='TertinaryLoad', blank=True, null=True)  # Field name made lowercase.
    quadrilateralload = models.IntegerField(db_column='QuadrilateralLoad', blank=True, null=True)  # Field name made lowercase.
    sdwanvpnip = models.CharField(db_column='SDWanVPNIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpnnetmask = models.CharField(db_column='SDWanVPNNetmask', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpndhcpstart = models.CharField(db_column='SDWanVPNDhcpStart', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpndhcpend = models.CharField(db_column='SDWanVPNDhcpEnd', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpnleaseinterval = models.CharField(db_column='SDWanVPNLeaseInterval', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpndomainname = models.CharField(db_column='SDWanVPNDomainName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdwanvpndnsprimary = models.CharField(db_column='SDWanVPNDnsPrimary', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwanvpndnssecondary = models.CharField(db_column='SDWanVPNDnsSecondary', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangreconcentratorip = models.CharField(db_column='SDWanGreConcentratorIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangrekey = models.CharField(db_column='SDWanGreKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdwangreip = models.CharField(db_column='SDWanGREIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangrenetmask = models.CharField(db_column='SDWanGRENetmask', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangredhcpstart = models.CharField(db_column='SDWanGREDhcpStart', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangredhcpend = models.CharField(db_column='SDWanGREDhcpEnd', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangreleaseinterval = models.CharField(db_column='SDWanGRELeaseInterval', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangredomainname = models.CharField(db_column='SDWanGREDomainName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdwangrednsprimary = models.CharField(db_column='SDWanGREDnsPrimary', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangrednssecondary = models.CharField(db_column='SDWanGREDnsSecondary', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangrefailover = models.IntegerField(db_column='SDWanGREFailover', blank=True, null=True)  # Field name made lowercase.
    sdwangreconcentratorfailoverip = models.CharField(db_column='SDWanGREConcentratorFailoverIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sdwangretype = models.CharField(db_column='SDWanGREType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_sdwan'


class ApSendEmailCount(models.Model):
    apid = models.IntegerField(db_column='ApId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_send_email_count'


class ApSsid(models.Model):
    ssidname = models.CharField(db_column='SSIDName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssidwpakey = models.CharField(db_column='SSIDWpaKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nasid = models.CharField(db_column='NASId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ciphertype = models.CharField(db_column='CipherType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftprotocol = models.CharField(db_column='FTProtocol', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobilitydomain = models.CharField(db_column='MobilityDomain', max_length=20, blank=True, null=True)  # Field name made lowercase.
    macfilterpolicy = models.CharField(db_column='MACFilterPolicy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    networkname = models.CharField(db_column='NetworkName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hours = models.CharField(db_column='Hours', max_length=24, blank=True, null=True)  # Field name made lowercase.
    associationretrydelay = models.IntegerField(db_column='AssociationRetryDelay', blank=True, null=True)  # Field name made lowercase.
    ssidhide = models.IntegerField(db_column='SSIDHide', blank=True, null=True)  # Field name made lowercase.
    ssidsecuritytype = models.IntegerField(db_column='SSIDSecurityType', blank=True, null=True)  # Field name made lowercase.
    fastbsstransition = models.IntegerField(db_column='FastBSSTransition', blank=True, null=True)  # Field name made lowercase.
    opportunistickeycaching_okc = models.IntegerField(db_column='OpportunisticKeyCaching_okc', blank=True, null=True)  # Field name made lowercase.
    optimizedconnectivityexperience_oce = models.IntegerField(db_column='OptimizedConnectivityExperience_OCE', blank=True, null=True)  # Field name made lowercase.
    preauthentication = models.IntegerField(db_column='PreAuthentication', blank=True, null=True)  # Field name made lowercase.
    dynamicvlan = models.IntegerField(db_column='DynamicVlan', blank=True, null=True)  # Field name made lowercase.
    clientisolation = models.IntegerField(db_column='ClientIsolation', blank=True, null=True)  # Field name made lowercase.
    managementframeprotection = models.IntegerField(db_column='ManagementFrameProtection', blank=True, null=True)  # Field name made lowercase.
    krackcountermeasures = models.IntegerField(db_column='KRACKCounterMeasures', blank=True, null=True)  # Field name made lowercase.
    ssidbroadcastingband = models.IntegerField(db_column='SSIDBroadcastingBand', blank=True, null=True)  # Field name made lowercase.
    externaldhcpenable = models.IntegerField(db_column='ExternalDHCPEnable', blank=True, null=True)  # Field name made lowercase.
    hotspotenable = models.PositiveIntegerField(db_column='HotspotEnable', blank=True, null=True)  # Field name made lowercase.
    ssidenable = models.PositiveIntegerField(db_column='SSIDEnable', blank=True, null=True)  # Field name made lowercase.
    ssidsecuredbykey = models.PositiveIntegerField(db_column='SSIDSecuredByKey', blank=True, null=True)  # Field name made lowercase.
    schedulingenable = models.IntegerField(db_column='SchedulingEnable', blank=True, null=True)  # Field name made lowercase.
    restrictatssid = models.IntegerField(db_column='RestrictAtSSID', blank=True, null=True)  # Field name made lowercase.
    restrictataaa = models.IntegerField(db_column='RestrictAtAAA', blank=True, null=True)  # Field name made lowercase.
    vlanenabled = models.IntegerField(db_column='VlanEnabled', blank=True, null=True)  # Field name made lowercase.
    clientassociationthreshold_rf = models.IntegerField(db_column='ClientAssociationThreshold_RF', blank=True, null=True)  # Field name made lowercase.
    radiusprofile = models.IntegerField(db_column='RadiusProfile', blank=True, null=True)  # Field name made lowercase.
    ssidsdwan = models.IntegerField(db_column='SSIDSDWan', blank=True, null=True)  # Field name made lowercase.
    wlanprofileid = models.ForeignKey(
        'ApWlanProfile', 
        models.DO_NOTHING, 
        db_column='WLanProfileId'
    )  # Field name made lowercase.
    maxclient = models.IntegerField(db_column='MaxClient', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_ssid'


class ApWlanProfile(models.Model):
    wlanprofilename = models.CharField(db_column='WLanProfileName', max_length=40)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_wlan_profile'




#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=WFH new Table AP configuration tabale management

class APConfigurationTemplate(models.Model):
    
    ApProfiles = models.ForeignKey(
            ApProfiles,
            on_delete=models.CASCADE
        )
    
    ApWlanProfile = models.ForeignKey(
            ApWlanProfile,
            on_delete=models.CASCADE
        )
    
    ApSdwan = models.ForeignKey(
            ApSdwan,
            on_delete=models.CASCADE
        )

    ApRadiusProfile = models.ForeignKey(
            ApRadiusProfile,
            on_delete=models.CASCADE
        )

    ApMacPolicyProfile = models.ForeignKey(
            ApMacPolicyProfile,
            on_delete=models.CASCADE
        )

    customer = models.ForeignKey(
        AdmCustomer, 
        models.DO_NOTHING, 
        db_column='CustomerId', 
    )  # Field name made lowercase.
    