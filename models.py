# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdCampaign(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    adweight = models.IntegerField(db_column='AdWeight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_campaign'


class AdCampaigngroup(models.Model):
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.IntegerField(db_column='AdGroupId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_campaigngroup'


class AdCampaignlocation(models.Model):
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_campaignlocation'


class AdCampaignlocationPost(models.Model):
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_campaignlocation_post'


class AdCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_category'


class AdConfig(models.Model):
    campaignid = models.IntegerField(db_column='CampaignId', blank=True, null=True)  # Field name made lowercase.
    fullscreenpre = models.IntegerField(db_column='FullScreenPre', blank=True, null=True)  # Field name made lowercase.
    overlaypre = models.CharField(db_column='OverlayPre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imagepre = models.CharField(db_column='ImagePre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    videopre = models.CharField(db_column='VideoPre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fixedsinglepre = models.CharField(db_column='FixedSinglePre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fixedmultiplepre = models.CharField(db_column='FixedMultiplePre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fullscreenpost = models.CharField(db_column='FullScreenPost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    overlaypost = models.CharField(db_column='OverlayPost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imagepost = models.CharField(db_column='ImagePost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    videopost = models.CharField(db_column='VideoPost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fixedsinglepost = models.CharField(db_column='FixedSinglePost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fixedmultiplepost = models.CharField(db_column='FixedMultiplePost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationall = models.IntegerField(db_column='LocationAll', blank=True, null=True)  # Field name made lowercase.
    countryall = models.IntegerField(db_column='CountryAll', blank=True, null=True)  # Field name made lowercase.
    stateall = models.IntegerField(db_column='StateAll', blank=True, null=True)  # Field name made lowercase.
    venueall = models.IntegerField(db_column='VenueAll', blank=True, null=True)  # Field name made lowercase.
    cityall = models.IntegerField(db_column='CityAll', blank=True, null=True)  # Field name made lowercase.
    configchanged = models.IntegerField(db_column='ConfigChanged', blank=True, null=True)  # Field name made lowercase.
    exclusiveconfig = models.IntegerField(db_column='ExclusiveConfig', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_config'


class AdConfigcity(models.Model):
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_configcity'


class AdConfigcountry(models.Model):
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_configcountry'


class AdConfiglocation(models.Model):
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_configlocation'


class AdConfigstate(models.Model):
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_configstate'


class AdConfigvenue(models.Model):
    venue = models.CharField(db_column='Venue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adcampaignid = models.IntegerField(db_column='AdCampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_configvenue'


class AdEntry(models.Model):
    adname = models.CharField(db_column='AdName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    admediaid = models.IntegerField(db_column='AdMediaId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    displaylink = models.CharField(db_column='DisplayLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destinationlink = models.CharField(db_column='DestinationLink', max_length=200, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    adlocation = models.CharField(db_column='AdLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    advideo = models.CharField(db_column='AdVideo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalimpressions = models.IntegerField(db_column='TotalImpressions', blank=True, null=True)  # Field name made lowercase.
    adimpressiontype = models.IntegerField(db_column='AdImpressionType', blank=True, null=True)  # Field name made lowercase.
    adminupload = models.IntegerField(db_column='AdminUpload', blank=True, null=True)  # Field name made lowercase.
    displaydays = models.CharField(db_column='DisplayDays', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpc = models.FloatField(db_column='Cpc', blank=True, null=True)  # Field name made lowercase.
    cpm = models.FloatField(db_column='Cpm', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adtype = models.CharField(db_column='AdType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    displayhours = models.CharField(db_column='DisplayHours', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fromage = models.IntegerField(db_column='FromAge', blank=True, null=True)  # Field name made lowercase.
    toage = models.IntegerField(db_column='ToAge', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_entry'


class AdGroup(models.Model):
    adgroupname = models.CharField(db_column='AdGroupName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_group'


class AdGroupmap(models.Model):
    groupid = models.IntegerField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    adid = models.IntegerField(db_column='AdId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_groupmap'


class AdLocationmap(models.Model):
    locationid = models.IntegerField(db_column='LocationId')  # Field name made lowercase.
    adid = models.ForeignKey(AdEntry, models.DO_NOTHING, db_column='AdId', blank=True, null=True)  # Field name made lowercase.
    adtype = models.CharField(db_column='AdType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    multipleallowed = models.CharField(db_column='MultipleAllowed', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_locationmap'


class AdLocationmapPost(models.Model):
    locationid = models.IntegerField(db_column='LocationId')  # Field name made lowercase.
    adid = models.IntegerField(db_column='AdId')  # Field name made lowercase.
    adtype = models.CharField(db_column='AdType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    multipleallowed = models.CharField(db_column='MultipleAllowed', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_locationmap_post'


class AdMedia(models.Model):
    image1 = models.CharField(db_column='Image1', max_length=254, blank=True, null=True)  # Field name made lowercase.
    imagesize1 = models.IntegerField(db_column='ImageSize1', blank=True, null=True)  # Field name made lowercase.
    imagedimension1 = models.CharField(db_column='ImageDimension1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imagetype1 = models.CharField(db_column='ImageType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    image2 = models.CharField(db_column='Image2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    imagesize2 = models.IntegerField(db_column='ImageSize2', blank=True, null=True)  # Field name made lowercase.
    imagedimension2 = models.CharField(db_column='ImageDimension2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imagetype2 = models.CharField(db_column='ImageType2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    image3 = models.CharField(db_column='Image3', max_length=254, blank=True, null=True)  # Field name made lowercase.
    imagesize3 = models.IntegerField(db_column='ImageSize3', blank=True, null=True)  # Field name made lowercase.
    imagedimension3 = models.CharField(db_column='ImageDimension3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imagetype3 = models.CharField(db_column='ImageType3', max_length=150, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    videoname = models.CharField(db_column='VideoName', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_media'


class AdStatistics(models.Model):
    admediaid = models.IntegerField(db_column='AdMediaId', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    impressionid = models.IntegerField(db_column='ImpressionId', blank=True, null=True)  # Field name made lowercase.
    adcloseclicked = models.CharField(db_column='AdCloseClicked', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adclosetime = models.DateTimeField(db_column='AdCloseTime', blank=True, null=True)  # Field name made lowercase.
    adpage = models.CharField(db_column='AdPage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calledstationid = models.CharField(db_column='CalledStationId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_statistics'


class AdStatuschanged(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    forcerecompute = models.IntegerField(db_column='ForceRecompute', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_statuschanged'


class AdTemptable(models.Model):
    campaignid = models.IntegerField(db_column='CampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    durationid = models.CharField(db_column='DurationId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adid = models.IntegerField(db_column='AdId', blank=True, null=True)  # Field name made lowercase.
    relativeweight = models.FloatField(db_column='RelativeWeight', blank=True, null=True)  # Field name made lowercase.
    displaycount = models.IntegerField(db_column='DisplayCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_temptable'


class AdmAccount(models.Model):
    username = models.CharField(db_column='UserName', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('AdmCustomer', models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    showpassword = models.IntegerField(db_column='ShowPassword', blank=True, null=True)  # Field name made lowercase.
    datecreate = models.DateTimeField(db_column='DateCreate', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='IsAdmin', blank=True, null=True)  # Field name made lowercase.
    accessprofileid = models.IntegerField(db_column='AccessProfileId', blank=True, null=True)  # Field name made lowercase.
    voucherscope = models.CharField(db_column='VoucherScope', max_length=6, blank=True, null=True)  # Field name made lowercase.
    customertype = models.IntegerField(db_column='CustomerType', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_account'


class AdmCustomer(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    signupdate = models.DateTimeField(db_column='SignupDate', blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    realm = models.CharField(db_column='Realm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logourl = models.CharField(db_column='LogoUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    homepage = models.CharField(db_column='HomePage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    voucherpassword = models.CharField(db_column='VoucherPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timezoneid = models.IntegerField(db_column='TimeZoneId', blank=True, null=True)  # Field name made lowercase.
    timezonename = models.CharField(db_column='TimezoneName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hasrestrictions = models.IntegerField(db_column='HasRestrictions', blank=True, null=True)  # Field name made lowercase.
    featureaccess = models.CharField(db_column='FeatureAccess', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=40, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=30, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dateformatid = models.IntegerField(db_column='DateFormatId', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    editspecialradius = models.IntegerField(db_column='EditSpecialRadius', blank=True, null=True)  # Field name made lowercase.
    enablebilling = models.IntegerField(db_column='EnableBilling', blank=True, null=True)  # Field name made lowercase.
    autologinpassword = models.CharField(db_column='AutoLoginPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    freeloginpassword = models.CharField(db_column='FreeLoginPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    savecvv = models.IntegerField(db_column='SaveCvv', blank=True, null=True)  # Field name made lowercase.
    savebilling = models.IntegerField(db_column='SaveBilling', blank=True, null=True)  # Field name made lowercase.
    haslanding = models.IntegerField(db_column='HasLanding', blank=True, null=True)  # Field name made lowercase.
    defaultvendor = models.CharField(db_column='DefaultVendor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portalversion = models.IntegerField(db_column='PortalVersion', blank=True, null=True)  # Field name made lowercase.
    enablebyod = models.IntegerField(db_column='EnableBYOD', blank=True, null=True)  # Field name made lowercase.
    enableads = models.IntegerField(db_column='EnableAds', blank=True, null=True)  # Field name made lowercase.
    enablesurvey = models.IntegerField(db_column='EnableSurvey', blank=True, null=True)  # Field name made lowercase.
    enablenms = models.IntegerField(db_column='EnableNMS', blank=True, null=True)  # Field name made lowercase.
    enablesocial = models.IntegerField(db_column='EnableSocial', blank=True, null=True)  # Field name made lowercase.
    enablemails = models.IntegerField(db_column='EnableMails', blank=True, null=True)  # Field name made lowercase.
    enablesms = models.IntegerField(db_column='EnableSMS', blank=True, null=True)  # Field name made lowercase.
    enableapmanagement = models.IntegerField(db_column='EnableAPManagement', blank=True, null=True)  # Field name made lowercase.
    enableroaming = models.IntegerField(db_column='EnableRoaming', blank=True, null=True)  # Field name made lowercase.
    billingemail = models.CharField(db_column='BillingEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billingperson = models.CharField(db_column='BillingPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billingfrequency = models.CharField(db_column='BillingFrequency', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datesuspended = models.DateTimeField(db_column='DateSuspended', blank=True, null=True)  # Field name made lowercase.
    suspendreason = models.CharField(db_column='SuspendReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enableldap = models.IntegerField(db_column='EnableLDAP', blank=True, null=True)  # Field name made lowercase.
    parentcustomerid = models.IntegerField(db_column='ParentCustomerId', blank=True, null=True)  # Field name made lowercase.
    customertype = models.IntegerField(db_column='CustomerType', blank=True, null=True)  # Field name made lowercase.
    captivesupportno = models.CharField(db_column='CaptiveSupportNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    logopath = models.CharField(db_column='LogoPath', max_length=150, blank=True, null=True)  # Field name made lowercase.
    googlemapkey = models.CharField(db_column='GoogleMapKey', max_length=250, blank=True, null=True)  # Field name made lowercase.
    uploadlogo = models.IntegerField(db_column='UploadLogo', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_customer'


class AdmCustomerInvoice(models.Model):
    invoicename = models.CharField(db_column='InvoiceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoicedescription = models.CharField(db_column='InvoiceDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    paybydate = models.DateTimeField(db_column='PayByDate', blank=True, null=True)  # Field name made lowercase.
    invoiceamount = models.FloatField(db_column='InvoiceAmount', blank=True, null=True)  # Field name made lowercase.
    invoicecurrency = models.CharField(db_column='InvoiceCurrency', max_length=3, blank=True, null=True)  # Field name made lowercase.
    invoicestatus = models.CharField(db_column='InvoiceStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gracedays = models.IntegerField(db_column='GraceDays', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    paidmethod = models.CharField(db_column='PaidMethod', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.FloatField(db_column='PaidAmount', blank=True, null=True)  # Field name made lowercase.
    paidtransactionid = models.CharField(db_column='PaidTransactionId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paidchequenumber = models.CharField(db_column='PaidChequeNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paidchequebankname = models.CharField(db_column='PaidChequeBankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoicefilename = models.CharField(db_column='InvoiceFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicefilepath = models.CharField(db_column='InvoiceFilePath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_customer_invoice'


class AdmDbchangehistory(models.Model):
    changedate = models.DateTimeField(db_column='ChangeDate', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=128)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    accountid = models.PositiveIntegerField(db_column='AccountId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_dbchangehistory'


class AdmFeatureaccess(models.Model):
    authusers = models.IntegerField(db_column='AuthUsers', blank=True, null=True)  # Field name made lowercase.
    authgroups = models.IntegerField(db_column='AuthGroups', blank=True, null=True)  # Field name made lowercase.
    authhotspots = models.IntegerField(db_column='AuthHotspots', blank=True, null=True)  # Field name made lowercase.
    authpolicy = models.IntegerField(db_column='AuthPolicy', blank=True, null=True)  # Field name made lowercase.
    authcaptiveportal = models.IntegerField(db_column='AuthCaptivePortal', blank=True, null=True)  # Field name made lowercase.
    manageap = models.IntegerField(db_column='ManageAp', blank=True, null=True)  # Field name made lowercase.
    manageunibox = models.IntegerField(db_column='ManageUnibox', blank=True, null=True)  # Field name made lowercase.
    manageswitches = models.IntegerField(db_column='ManageSwitches', blank=True, null=True)  # Field name made lowercase.
    billingplans = models.IntegerField(db_column='BillingPlans', blank=True, null=True)  # Field name made lowercase.
    billingconfig = models.IntegerField(db_column='BillingConfig', blank=True, null=True)  # Field name made lowercase.
    billingrevenueshare = models.IntegerField(db_column='BillingRevenueShare', blank=True, null=True)  # Field name made lowercase.
    billingvouchers = models.IntegerField(db_column='BillingVouchers', blank=True, null=True)  # Field name made lowercase.
    billingvoucherdesign = models.IntegerField(db_column='BillingVoucherDesign', blank=True, null=True)  # Field name made lowercase.
    crmtickets = models.IntegerField(db_column='CRMTickets', blank=True, null=True)  # Field name made lowercase.
    crmemailtemplates = models.IntegerField(db_column='CRMEmailTemplates', blank=True, null=True)  # Field name made lowercase.
    advertisement = models.IntegerField(db_column='Advertisement', blank=True, null=True)  # Field name made lowercase.
    adminaccounts = models.PositiveIntegerField(db_column='AdminAccounts', blank=True, null=True)  # Field name made lowercase.
    cfilter = models.IntegerField(db_column='CFilter', blank=True, null=True)  # Field name made lowercase.
    customertype = models.PositiveIntegerField(db_column='CustomerType', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    authautologin = models.IntegerField(db_column='AuthAutoLogin', blank=True, null=True)  # Field name made lowercase.
    authsms = models.IntegerField(db_column='AuthSms', blank=True, null=True)  # Field name made lowercase.
    proximity = models.IntegerField(db_column='Proximity', blank=True, null=True)  # Field name made lowercase.
    survey = models.IntegerField(db_column='Survey', blank=True, null=True)  # Field name made lowercase.
    automatedrep = models.IntegerField(db_column='AutomatedRep', blank=True, null=True)  # Field name made lowercase.
    selfcarelogin = models.IntegerField(db_column='SelfCareLogin', blank=True, null=True)  # Field name made lowercase.
    reviews = models.IntegerField(db_column='Reviews', blank=True, null=True)  # Field name made lowercase.
    networkprofiles = models.IntegerField(db_column='NetworkProfiles', blank=True, null=True)  # Field name made lowercase.
    smstemplates = models.IntegerField(db_column='SMSTemplates', blank=True, null=True)  # Field name made lowercase.
    managereseller = models.IntegerField(db_column='ManageReseller', blank=True, null=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId', blank=True, null=True)  # Field name made lowercase.
    rogueap = models.IntegerField(db_column='RogueAp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_featureaccess'


class AdmHotspotPlantype(models.Model):
    planname = models.CharField(db_column='PlanName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    planusers = models.IntegerField(db_column='PlanUsers', blank=True, null=True)  # Field name made lowercase.
    defaultfee = models.FloatField(db_column='DefaultFee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_hotspot_plantype'


class AdmLoginhistory(models.Model):
    accountname = models.CharField(db_column='AccountName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='LoginDate', blank=True, null=True)  # Field name made lowercase.
    logoutdate = models.DateTimeField(db_column='LogoutDate', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_loginhistory'


class AdmMailConfig(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    scriptcode = models.CharField(db_column='ScriptCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    opcode = models.CharField(db_column='OpCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_mail_config'


class AdmTimediff(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=5, blank=True, null=True)  # Field name made lowercase.
    difference = models.CharField(db_column='Difference', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_timediff'


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


class ApEmailAlert(models.Model):
    apid = models.CharField(db_column='ApId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    lastcheckintime = models.CharField(db_column='LastCheckInTime', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_email_alert'


class ApFloormap(models.Model):
    apid = models.IntegerField(db_column='Apid', unique=True, blank=True, null=True)  # Field name made lowercase.
    floorid = models.IntegerField(db_column='Floorid', blank=True, null=True)  # Field name made lowercase.
    xcord = models.FloatField(db_column='Xcord', blank=True, null=True)  # Field name made lowercase.
    ycord = models.FloatField(db_column='Ycord', blank=True, null=True)  # Field name made lowercase.
    applacedate = models.DateTimeField()
    applaceupdateddate = models.DateTimeField()
    floorimgheight = models.FloatField(blank=True, null=True)
    floorimgwidth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ap_floormap'


class ApLifeCycle(models.Model):
    apid = models.ForeignKey(Ap, models.DO_NOTHING, db_column='ApId')  # Field name made lowercase.
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocationId')  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    aplife = models.TextField(db_column='ApLife')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_life_cycle'


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
    wlanprofileid = models.ForeignKey('ApWlanProfile', models.DO_NOTHING, db_column='WLanProfileId')  # Field name made lowercase.
    maxclient = models.IntegerField(db_column='MaxClient', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_ssid'


class ApWips(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    wipsenable = models.IntegerField(db_column='WIPSEnable', blank=True, null=True)  # Field name made lowercase.
    roguerfcutoffthreshold = models.IntegerField(db_column='RogueRFCutoffThreshold')  # Field name made lowercase.
    reportedbynoaps = models.IntegerField(db_column='ReportedByNoAps', blank=True, null=True)  # Field name made lowercase.
    advertisesunsecuredssids = models.CharField(db_column='AdvertisesUnsecuredSSIDs', max_length=50)  # Field name made lowercase.
    advertisesauthorizedssids = models.CharField(db_column='AdvertisesAuthorizedSSIDs', max_length=50)  # Field name made lowercase.
    advertisesfollowingssids = models.CharField(db_column='AdvertisesFollowingSSIDs', max_length=50)  # Field name made lowercase.
    enablerogueapdetection = models.IntegerField(db_column='EnableRogueAPDetection', blank=True, null=True)  # Field name made lowercase.
    enablehoneypoteviltwindetection = models.IntegerField(db_column='EnableHoneypotEvilTwinDetection', blank=True, null=True)  # Field name made lowercase.
    enablemisconfiguredapdetection = models.IntegerField(db_column='EnableMisconfiguredAPDetection', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_wips'


class ApWlanProfile(models.Model):
    wlanprofilename = models.CharField(db_column='WLanProfileName', max_length=40)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_wlan_profile'


class Bill2CheckoutTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_2checkout_temp'


class Bill2CheckoutTransaction(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='OrderNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoiceid = models.CharField(db_column='InvoiceId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pay_method = models.CharField(max_length=10, blank=True, null=True)
    credit_card_processed = models.CharField(max_length=10, blank=True, null=True)
    hashkey = models.CharField(db_column='HashKey', max_length=150, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_2checkout_transaction'


class BillAllTransaction(models.Model):
    gatewaytypeid = models.IntegerField(db_column='GatewayTypeId')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    responsecode = models.CharField(db_column='ResponseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    transactiontype = models.CharField(db_column='TransactionType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(db_column='ErrorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    pendingreason = models.CharField(db_column='PendingReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_all_transaction'


class BillAppliedpromotion(models.Model):
    promotionid = models.PositiveIntegerField(db_column='PromotionId', blank=True, null=True)  # Field name made lowercase.
    applieddate = models.DateTimeField(db_column='AppliedDate', blank=True, null=True)  # Field name made lowercase.
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    appliedamount = models.CharField(db_column='AppliedAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_appliedpromotion'


class BillAtomTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    atompaymentid = models.CharField(db_column='AtomPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_atom_temp'


class BillAtomTransaction(models.Model):
    userid = models.PositiveIntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billingemail = models.CharField(db_column='BillingEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    am_paymentid = models.CharField(db_column='AM_PaymentId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    am_transactionid = models.CharField(db_column='AM_TransactionId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    am_banktransactionid = models.CharField(db_column='AM_BankTransactionId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transactionstatus = models.CharField(db_column='TransactionStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transactiontype = models.CharField(db_column='TransactionType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    surcharge = models.PositiveIntegerField(db_column='Surcharge', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    clientcode = models.IntegerField(db_column='ClientCode', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descriminator = models.CharField(db_column='Descriminator', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.PositiveIntegerField(db_column='CardNumber', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeremailid = models.CharField(db_column='CustomerEmailId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customermobilenumber = models.CharField(db_column='CustomerMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=150, blank=True, null=True)  # Field name made lowercase.
    merchantdata = models.CharField(db_column='MerchantData', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_atom_transaction'


class BillAuthnetBackup(models.Model):
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    auth_responsecode = models.CharField(db_column='Auth_ResponseCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_responsesubcode = models.CharField(db_column='Auth_ResponseSubcode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_reasoncode = models.CharField(db_column='Auth_ReasonCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_reasoncodetext = models.CharField(db_column='Auth_ReasonCodeText', max_length=150, blank=True, null=True)  # Field name made lowercase.
    auth_approvalcode = models.CharField(db_column='Auth_ApprovalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_avsresultcode = models.CharField(db_column='Auth_AVSResultCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_transactionid = models.CharField(db_column='Auth_TransactionID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_cvvresponsecode = models.CharField(db_column='Auth_CVVResponseCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_invoicenumber = models.CharField(db_column='Auth_InvoiceNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_method = models.CharField(db_column='Auth_Method', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_authnet_backup'


class BillAuthnetPaymentinfo(models.Model):
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cardexpirydate = models.DateField(db_column='CardExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cvvnumber = models.CharField(db_column='CvvNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextbillingdate = models.DateTimeField(db_column='NextBillingDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_authnet_paymentinfo'


class BillAuthnetTransaction(models.Model):
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    auth_responsecode = models.CharField(db_column='Auth_ResponseCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_responsesubcode = models.CharField(db_column='Auth_ResponseSubcode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_reasoncode = models.CharField(db_column='Auth_ReasonCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_reasoncodetext = models.CharField(db_column='Auth_ReasonCodeText', max_length=150, blank=True, null=True)  # Field name made lowercase.
    auth_approvalcode = models.CharField(db_column='Auth_ApprovalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_avsresultcode = models.CharField(db_column='Auth_AVSResultCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_transactionid = models.CharField(db_column='Auth_TransactionID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    auth_cvvresponsecode = models.CharField(db_column='Auth_CVVResponseCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    auth_invoicenumber = models.CharField(db_column='Auth_InvoiceNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_method = models.CharField(db_column='Auth_Method', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_authnet_transaction'


class BillBilldeskTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    bdpaymentid = models.CharField(db_column='BdPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_billdesk_temp'


class BillBilldeskTransaction(models.Model):
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bd_paymentid = models.CharField(db_column='Bd_PaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bd_txnrefno = models.CharField(db_column='Bd_TxnRefNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bd_bankrefno = models.CharField(db_column='Bd_BankRefNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bd_bankid = models.CharField(db_column='Bd_BankId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bd_bankmerchantid = models.CharField(db_column='Bd_BankMerchantId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bd_currency = models.CharField(db_column='Bd_Currency', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bd_errorcode = models.CharField(db_column='Bd_ErrorCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bd_errordesc = models.CharField(db_column='Bd_ErrorDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mpaymentid = models.CharField(db_column='MPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.CharField(db_column='TranStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountfee = models.CharField(db_column='AmountFee', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountnet = models.CharField(db_column='AmountNet', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    bd_responsecode = models.CharField(db_column='Bd_ResponseCode', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_billdesk_transaction'


class BillCcavenueTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    cc_orderid = models.CharField(db_column='CC_OrderId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_ccavenue_temp'


class BillCcavenueTransaction(models.Model):
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    cc_orderid = models.CharField(db_column='CC_OrderId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cc_trackingid = models.CharField(db_column='CC_TrackingId', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cc_bankrefno = models.CharField(db_column='CC_BankRefNo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cc_orderstatus = models.CharField(db_column='CC_OrderStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cc_failuremessage = models.CharField(db_column='CC_FailureMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cc_paymentmode = models.CharField(db_column='CC_PaymentMode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cc_statuscode = models.CharField(db_column='CC_StatusCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cc_statusmessage = models.CharField(db_column='CC_StatusMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cc_vault = models.CharField(db_column='CC_Vault', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cc_offertype = models.CharField(db_column='CC_OfferType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cc_offercode = models.CharField(db_column='CC_OfferCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=3, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_ccavenue_transaction'


class BillConfig(models.Model):
    cycletime = models.IntegerField(db_column='CycleTime', blank=True, null=True)  # Field name made lowercase.
    cyclefrequency = models.IntegerField(db_column='CycleFrequency', blank=True, null=True)  # Field name made lowercase.
    nextbillingdate = models.DateTimeField(db_column='NextBillingDate', blank=True, null=True)  # Field name made lowercase.
    lastbillingdate = models.DateTimeField(db_column='LastBillingDate', blank=True, null=True)  # Field name made lowercase.
    billingemailaddress = models.CharField(db_column='BillingEmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxfailedattempts = models.IntegerField(db_column='MaxFailedAttempts', blank=True, null=True)  # Field name made lowercase.
    notifyregistration = models.IntegerField(db_column='NotifyRegistration', blank=True, null=True)  # Field name made lowercase.
    registrationemails = models.CharField(db_column='RegistrationEmails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    summaryemails = models.CharField(db_column='SummaryEmails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    confirmtemplateid = models.PositiveIntegerField(db_column='ConfirmTemplateId', blank=True, null=True)  # Field name made lowercase.
    receipttemplateid = models.PositiveIntegerField(db_column='ReceiptTemplateId', blank=True, null=True)  # Field name made lowercase.
    carddeclinetemplateid = models.PositiveIntegerField(db_column='CardDeclineTemplateId', blank=True, null=True)  # Field name made lowercase.
    cardexpiringtemplateid = models.PositiveIntegerField(db_column='CardExpiringTemplateId', blank=True, null=True)  # Field name made lowercase.
    releaseonsuccess = models.IntegerField(db_column='ReleaseOnSuccess', blank=True, null=True)  # Field name made lowercase.
    verifycardupdate = models.IntegerField(db_column='VerifyCardUpdate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    onfailaction = models.IntegerField(db_column='OnFailAction', blank=True, null=True)  # Field name made lowercase.
    restrictedgroup = models.CharField(db_column='RestrictedGroup', max_length=30, blank=True, null=True)  # Field name made lowercase.
    renewtemplateid = models.IntegerField(db_column='RenewTemplateId', blank=True, null=True)  # Field name made lowercase.
    expiredtemplateid = models.IntegerField(db_column='ExpiredTemplateId', blank=True, null=True)  # Field name made lowercase.
    dailysignupemails = models.CharField(db_column='DailySignupEmails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smstemplateid = models.IntegerField(db_column='SmsTemplateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_config'


class BillEchoTransaction(models.Model):
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    echo_authcode = models.CharField(db_column='Echo_AuthCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    echo_avsresult = models.CharField(db_column='Echo_AVSResult', max_length=3, blank=True, null=True)  # Field name made lowercase.
    echo_declinecode = models.CharField(db_column='Echo_DeclineCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    echo_reference = models.CharField(db_column='Echo_Reference', max_length=10, blank=True, null=True)  # Field name made lowercase.
    echo_mac = models.CharField(db_column='Echo_Mac', max_length=2, blank=True, null=True)  # Field name made lowercase.
    echo_merchantname = models.CharField(db_column='Echo_MerchantName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    echo_merchanttracenbr = models.CharField(db_column='Echo_MerchantTraceNbr', max_length=10, blank=True, null=True)  # Field name made lowercase.
    echo_securityresult = models.CharField(db_column='Echo_SecurityResult', max_length=3, blank=True, null=True)  # Field name made lowercase.
    echo_status = models.CharField(db_column='Echo_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    echo_termcode = models.CharField(db_column='Echo_TermCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    echo_ordernumber = models.CharField(db_column='Echo_OrderNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    echo_version = models.CharField(db_column='Echo_Version', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=8, blank=True, null=True)  # Field name made lowercase.
    trandate = models.CharField(db_column='TranDate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=5, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_echo_transaction'


class BillEnkapTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    ordertransactionid = models.CharField(db_column='orderTransactionId', max_length=50)  # Field name made lowercase.
    merchantreferenceid = models.CharField(db_column='MerchantReferenceId', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_enkap_temp'


class BillEnkapTransaction(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    ordertransactionid = models.CharField(db_column='orderTransactionId', max_length=50)  # Field name made lowercase.
    merchantreferenceid = models.CharField(db_column='MerchantReferenceId', max_length=50)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=50)  # Field name made lowercase.
    paymentprovidername = models.CharField(db_column='paymentProviderName', max_length=50)  # Field name made lowercase.
    paymentproviderid = models.CharField(db_column='paymentProviderId', max_length=150)  # Field name made lowercase.
    totalamount = models.CharField(db_column='totalAmount', max_length=50)  # Field name made lowercase.
    currency = models.CharField(max_length=50)
    paymentdate = models.DateTimeField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    enakaptempid = models.CharField(db_column='EnakapTempId', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_enkap_transaction'


class BillEpayTransaction(models.Model):
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    epay_status = models.CharField(db_column='EPay_Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epay_result = models.CharField(db_column='EPay_Result', max_length=5, blank=True, null=True)  # Field name made lowercase.
    epay_resultcode = models.CharField(db_column='EPay_ResultCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    epay_authcode = models.CharField(db_column='EPay_AuthCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epay_refnum = models.CharField(db_column='EPay_RefNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epay_error = models.CharField(db_column='EPay_Error', max_length=100, blank=True, null=True)  # Field name made lowercase.
    epay_errorcode = models.CharField(db_column='EPay_ErrorCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    epay_avsresultcode = models.CharField(db_column='EPay_AVSResultCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epay_cvvresultcode = models.CharField(db_column='EPay_CVVResultCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auth_method = models.CharField(db_column='Auth_Method', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_epay_transaction'


class BillFlutterstdTransaction(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    txid = models.CharField(max_length=50, blank=True, null=True)
    txref = models.CharField(max_length=50, blank=True, null=True)
    devicefingerprint = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=40, blank=True, null=True)
    chargecode = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    paymenttype = models.CharField(max_length=40, blank=True, null=True)
    paymentid = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    expirymonth = models.IntegerField(blank=True, null=True)
    expiryyear = models.IntegerField(blank=True, null=True)
    cardbin = models.IntegerField(db_column='cardBIN', blank=True, null=True)  # Field name made lowercase.
    last4digits = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    fluttertempid = models.CharField(db_column='flutterTempId', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_flutterstd_transaction'


class BillFlutterwaveTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_flutterwave_temp'


class BillGateway(models.Model):
    gatewaytypeid = models.PositiveIntegerField(db_column='GatewayTypeId', blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    publickey = models.CharField(db_column='PublicKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    secretkey = models.CharField(db_column='SecretKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    testmode = models.IntegerField(db_column='TestMode', blank=True, null=True)  # Field name made lowercase.
    paypalusername = models.CharField(db_column='PaypalUserName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    partner = models.CharField(db_column='Partner', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=30, blank=True, null=True)  # Field name made lowercase.
    redirectserverip = models.CharField(db_column='RedirectServerIp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encryptionkey = models.CharField(db_column='EncryptionKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usagetype = models.IntegerField(db_column='UsageType', blank=True, null=True)  # Field name made lowercase.
    enabledfor = models.CharField(db_column='EnabledFor', max_length=3, blank=True, null=True)  # Field name made lowercase.
    enabledforid = models.IntegerField(db_column='EnabledForId', blank=True, null=True)  # Field name made lowercase.
    isenabled = models.IntegerField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_gateway'


class BillGatewaytype(models.Model):
    gatewayname = models.CharField(db_column='GatewayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='VendorName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gatewayurl = models.CharField(db_column='GatewayUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    testmode = models.IntegerField(db_column='TestMode', blank=True, null=True)  # Field name made lowercase.
    testgatewayurl = models.CharField(db_column='TestGatewayUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adaptersupport = models.IntegerField(db_column='AdapterSupport', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    debug = models.IntegerField(db_column='Debug', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_gatewaytype'


class BillInstamojoTemp(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=100, blank=True, null=True)  # Field name made lowercase.
    redirect_url = models.CharField(max_length=100, blank=True, null=True)
    webhook = models.CharField(max_length=100, blank=True, null=True)
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    mpaymentid = models.CharField(db_column='MPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.CharField(db_column='IsRenew', max_length=5, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_instamojo_temp'


class BillInstamojoTransaction(models.Model):
    paymentid = models.CharField(db_column='PaymentId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fees = models.CharField(db_column='Fees', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clientmac = models.CharField(db_column='ClientMAC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.CharField(db_column='UnitPrice', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    offerslug = models.CharField(db_column='OfferSlug', max_length=20, blank=True, null=True)  # Field name made lowercase.
    offertitle = models.CharField(db_column='OfferTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.CharField(db_column='DateCreated', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationid = models.CharField(db_column='LocationId', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_instamojo_transaction'


class BillMonetbilTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    paymentref = models.CharField(db_column='PaymentRef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentid = models.CharField(db_column='PaymentId', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_monetbil_temp'


class BillMonetbilTransaction(models.Model):
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billingphoneno = models.CharField(db_column='BillingPhoneNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingemail = models.CharField(db_column='BillingEmail', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingcity = models.CharField(db_column='BillingCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    billingzipcode = models.CharField(db_column='BillingZipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    billingcountry = models.CharField(db_column='BillingCountry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingipaddress = models.CharField(db_column='BillingIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mb_service = models.CharField(db_column='MB_Service', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mb_paymentid = models.CharField(db_column='MB_PaymentId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mb_status = models.IntegerField(db_column='MB_Status', blank=True, null=True)  # Field name made lowercase.
    mb_message = models.CharField(db_column='MB_Message', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mb_paymentref = models.CharField(db_column='MB_PaymentRef', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mb_itemref = models.CharField(db_column='MB_ItemRef', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mb_currency = models.CharField(db_column='MB_Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mb_fee = models.CharField(db_column='MB_Fee', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mb_revenue = models.CharField(db_column='MB_Revenue', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_monetbil_transaction'


class BillPayfastTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    mpaymentid = models.CharField(db_column='MPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payfast_temp'


class BillPayfaststdTransaction(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pfpaymentid = models.CharField(db_column='PfPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mpaymentid = models.CharField(db_column='MPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.CharField(db_column='TranStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountfee = models.CharField(db_column='AmountFee', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountnet = models.CharField(db_column='AmountNet', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payfaststd_transaction'


class BillPayflowTransaction(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase.
    pnref = models.CharField(db_column='PNREF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cvv2match = models.IntegerField(db_column='CVV2MATCH', blank=True, null=True)  # Field name made lowercase.
    respmsg = models.CharField(db_column='RESPMSG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authcode = models.CharField(db_column='AUTHCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payflow_transaction'


class BillPaymentinfo(models.Model):
    businessname = models.CharField(db_column='BusinessName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=40, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=30, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cardname = models.CharField(db_column='CardName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cardexpirydate = models.DateField(db_column='CardExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cardzipcode = models.CharField(db_column='CardZipcode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cvvnumber = models.CharField(db_column='CvvNumber', max_length=5, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_paymentinfo'


class BillPaypalBackup(models.Model):
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    paypal_ack = models.CharField(db_column='Paypal_Ack', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_errorcode = models.CharField(db_column='Paypal_ErrorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_longmessage = models.CharField(db_column='Paypal_LongMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paypal_shortmessage = models.CharField(db_column='Paypal_ShortMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paypal_avscode = models.CharField(db_column='Paypal_AVSCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paypal_cvv2code = models.CharField(db_column='Paypal_CVV2Code', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paypal_transactionid = models.CharField(db_column='Paypal_TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paypal_correlationid = models.CharField(db_column='Paypal_CorrelationID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paypal_timestamp = models.CharField(db_column='Paypal_Timestamp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paypal_version = models.CharField(db_column='Paypal_Version', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_build = models.CharField(db_column='Paypal_Build', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_paypal_backup'


class BillPaypalTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_paypal_temp'


class BillPaypalTransaction(models.Model):
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    paypal_ack = models.CharField(db_column='Paypal_Ack', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paypal_errorcode = models.CharField(db_column='Paypal_ErrorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_longmessage = models.CharField(db_column='Paypal_LongMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paypal_shortmessage = models.CharField(db_column='Paypal_ShortMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paypal_avscode = models.CharField(db_column='Paypal_AVSCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paypal_cvv2code = models.CharField(db_column='Paypal_CVV2Code', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paypal_transactionid = models.CharField(db_column='Paypal_TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paypal_correlationid = models.CharField(db_column='Paypal_CorrelationID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paypal_timestamp = models.CharField(db_column='Paypal_Timestamp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paypal_version = models.CharField(db_column='Paypal_Version', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_build = models.CharField(db_column='Paypal_Build', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_paypal_transaction'


class BillPaypalstdTransaction(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paypal_responsemessage = models.CharField(db_column='Paypal_ResponseMessage', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paypal_errorcode = models.CharField(db_column='Paypal_ErrorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal_transactionid = models.CharField(db_column='Paypal_TransactionID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paypal_responsecode = models.CharField(db_column='PayPal_ResponseCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    paypal_pendingreason = models.CharField(db_column='Paypal_PendingReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    paypaltempid = models.CharField(db_column='PayPalTempId', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_paypalstd_transaction'


class BillPayprinAxisTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payprin_axis_temp'


class BillPayprinAxisTransaction(models.Model):
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    payprin_axis_invoice = models.CharField(db_column='Payprin_Axis_Invoice', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_transactionid = models.CharField(db_column='Payprin_Axis_TransactionID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_authcode = models.CharField(db_column='Payprin_Axis_AuthCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_avscode = models.CharField(db_column='Payprin_Axis_AVSCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_cvv2code = models.CharField(db_column='Payprin_Axis_CVV2Code', max_length=5, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_errorcode = models.CharField(db_column='Payprin_Axis_ErrorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_responsecode = models.CharField(db_column='Payprin_Axis_ResponseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_transstatus = models.CharField(db_column='Payprin_Axis_TransStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_tranamount = models.CharField(db_column='Payprin_Axis_TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payprin_axis_trantype = models.CharField(db_column='Payprin_Axis_TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payprin_axis_transaction'


class BillPayuTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    payupaymentid = models.CharField(db_column='PayUPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payu_temp'


class BillPayuTransaction(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pu_payutransactionid = models.CharField(db_column='PU_PayUTransactionId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pu_transactionid = models.CharField(db_column='PU_TransactionId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pu_transactionstatus = models.CharField(db_column='PU_TransactionStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pu_returncode = models.CharField(db_column='PU_ReturnCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pu_transactiontype = models.CharField(db_column='PU_TransactionType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.CharField(db_column='TranStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountfee = models.CharField(db_column='AmountFee', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amountnet = models.CharField(db_column='AmountNet', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payu_transaction'


class BillPayumoneyTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hashstring = models.CharField(db_column='HashString', max_length=300, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    paymentid = models.CharField(db_column='PaymentId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payumoney_temp'


class BillPayzenTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    payzenpaymentid = models.CharField(db_column='PayzenPaymentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payzen_temp'


class BillPayzenTransaction(models.Model):
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    vads_auth_number = models.CharField(db_column='Vads_Auth_Number', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vads_auth_result = models.IntegerField(db_column='Vads_Auth_Result', blank=True, null=True)  # Field name made lowercase.
    vads_site_id = models.IntegerField(db_column='Vads_Site_Id', blank=True, null=True)  # Field name made lowercase.
    vads_trans_id = models.IntegerField(db_column='Vads_Trans_Id', blank=True, null=True)  # Field name made lowercase.
    vads_warranty_result = models.CharField(db_column='Vads_Warranty_Result', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vads_payment_src = models.CharField(db_column='Vads_Payment_Src', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vads_bank_product = models.CharField(db_column='Vads_Bank_Product', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vads_operation_type = models.CharField(db_column='Vads_Operation_Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vads_threeds_status = models.CharField(db_column='Vads_Threeds_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vads_result = models.IntegerField(db_column='Vads_Result', blank=True, null=True)  # Field name made lowercase.
    vads_card_country = models.CharField(db_column='Vads_Card_Country', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vads_language = models.CharField(db_column='Vads_Language', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vads_page_action = models.CharField(db_column='Vads_Page_Action', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=3, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_payzen_transaction'


class BillPlan(models.Model):
    planname = models.CharField(db_column='PlanName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginpolicyid = models.IntegerField(db_column='LoginPolicyId')  # Field name made lowercase.
    setupfee = models.CharField(db_column='SetupFee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recurringfee = models.CharField(db_column='RecurringFee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    billingcycle = models.IntegerField(db_column='BillingCycle', blank=True, null=True)  # Field name made lowercase.
    billinginterval = models.IntegerField(db_column='BillingInterval', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    totalclients = models.IntegerField(db_column='TotalClients', blank=True, null=True)  # Field name made lowercase.
    plantype = models.IntegerField(db_column='PlanType', blank=True, null=True)  # Field name made lowercase.
    plangroupid = models.IntegerField(db_column='PlanGroupId', blank=True, null=True)  # Field name made lowercase.
    usergroupid = models.IntegerField(db_column='UserGroupId', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concurrencylimit = models.PositiveSmallIntegerField(db_column='ConcurrencyLimit', blank=True, null=True)  # Field name made lowercase.
    downloadrate = models.PositiveSmallIntegerField(db_column='DownloadRate', blank=True, null=True)  # Field name made lowercase.
    downloadrateunit = models.PositiveSmallIntegerField(db_column='DownloadRateUnit', blank=True, null=True)  # Field name made lowercase.
    uploadrate = models.PositiveSmallIntegerField(db_column='UploadRate', blank=True, null=True)  # Field name made lowercase.
    uploadrateunit = models.PositiveSmallIntegerField(db_column='UploadRateUnit', blank=True, null=True)  # Field name made lowercase.
    fupdatarate = models.IntegerField(db_column='FupDataRate', blank=True, null=True)  # Field name made lowercase.
    fupdatarateunit = models.IntegerField(db_column='FupDataRateUnit', blank=True, null=True)  # Field name made lowercase.
    fupdownloadrate = models.IntegerField(db_column='FupDownloadRate', blank=True, null=True)  # Field name made lowercase.
    fupdownloadrateunit = models.IntegerField(db_column='FupDownloadRateUnit', blank=True, null=True)  # Field name made lowercase.
    fupuploadrate = models.IntegerField(db_column='FupUploadRate', blank=True, null=True)  # Field name made lowercase.
    fupuploadrateunit = models.IntegerField(db_column='FupUploadRateUnit', blank=True, null=True)  # Field name made lowercase.
    planrestriction = models.IntegerField(db_column='PlanRestriction', blank=True, null=True)  # Field name made lowercase.
    smscountperuserperdevice = models.IntegerField(db_column='SMSCountPerUserPerDevice', blank=True, null=True)  # Field name made lowercase.
    planaccesstype = models.IntegerField(db_column='PlanAccessType')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_plan'


class BillPlangroup(models.Model):
    plangroupname = models.CharField(db_column='PlanGroupName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_plangroup'


class BillPlanmap(models.Model):
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_planmap'


class BillProsaTemp(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transamount = models.CharField(db_column='TransAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdatarequired = models.IntegerField(db_column='BillDataRequired', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    prosaorderid = models.CharField(db_column='ProsaOrderId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prosadigest = models.CharField(db_column='ProsaDigest', max_length=100, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_prosa_temp'


class BillProsaTransaction(models.Model):
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    prosa_response = models.CharField(db_column='Prosa_Response', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prosa_orderid = models.CharField(db_column='Prosa_OrderId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prosa_merchant = models.CharField(db_column='Prosa_Merchant', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prosa_store = models.CharField(db_column='Prosa_Store', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prosa_term = models.CharField(db_column='Prosa_Term', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prosa_refnum = models.CharField(db_column='Prosa_RefNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prosa_auth = models.IntegerField(db_column='Prosa_Auth', blank=True, null=True)  # Field name made lowercase.
    prosa_digest = models.CharField(db_column='Prosa_Digest', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.CharField(db_column='TranStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_prosa_transaction'


class BillStripeTemp(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='AptNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    successurl = models.CharField(db_column='SuccessUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    failurl = models.CharField(db_column='FailUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_stripe_temp'


class BillStripeTransaction(models.Model):
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customeremailid = models.CharField(db_column='CustomerEmailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customermobilenumber = models.CharField(db_column='CustomerMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stripetoken = models.CharField(db_column='StripeToken', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stripeemail = models.CharField(db_column='StripeEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='ORDERID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    txnamount = models.CharField(db_column='TXNAMOUNT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    txndate = models.DateTimeField(db_column='TXNDATE', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stripeid = models.CharField(db_column='StripeId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stripeobject = models.CharField(db_column='StripeObject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stripeamount = models.CharField(db_column='StripeAmount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amount_refunded = models.CharField(max_length=100, blank=True, null=True)
    balance_transaction = models.CharField(max_length=100, blank=True, null=True)
    captured = models.CharField(max_length=20, blank=True, null=True)
    created = models.CharField(max_length=20, blank=True, null=True)
    stripecurrency = models.CharField(db_column='StripeCurrency', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stripecustomer = models.CharField(db_column='StripeCustomer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stripedescription = models.CharField(db_column='StripeDescription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    failure_code = models.CharField(max_length=50, blank=True, null=True)
    failure_message = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    seller_message = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    paid = models.CharField(max_length=50, blank=True, null=True)
    refunded = models.CharField(max_length=50, blank=True, null=True)
    total_count = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)
    sourceid = models.CharField(db_column='sourceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourceobject = models.CharField(db_column='sourceObject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(max_length=50, blank=True, null=True)
    address_country = models.CharField(max_length=50, blank=True, null=True)
    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    address_line1_check = models.CharField(max_length=50, blank=True, null=True)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    address_state = models.CharField(max_length=50, blank=True, null=True)
    address_zip = models.CharField(max_length=50, blank=True, null=True)
    address_zip_check = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    customer = models.CharField(max_length=50, blank=True, null=True)
    cvc_check = models.CharField(max_length=50, blank=True, null=True)
    exp_month = models.CharField(max_length=50, blank=True, null=True)
    exp_year = models.CharField(max_length=50, blank=True, null=True)
    fingerprint = models.CharField(max_length=50, blank=True, null=True)
    funding = models.CharField(max_length=50, blank=True, null=True)
    last4 = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    source_transfer = models.CharField(max_length=50, blank=True, null=True)
    statement_descriptor = models.CharField(max_length=50, blank=True, null=True)
    stripestatus = models.CharField(db_column='StripeStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_stripe_transaction'


class BillUgmartTransaction(models.Model):
    userid = models.PositiveIntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    ug_responsecode = models.CharField(db_column='UG_ResponseCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ug_status = models.CharField(db_column='UG_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ug_message = models.CharField(db_column='UG_Message', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ug_transactionid = models.CharField(db_column='UG_TransactionID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ug_method = models.CharField(db_column='UG_Method', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ug_chargedamount = models.CharField(db_column='UG_ChargedAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ug_commission = models.CharField(db_column='UG_Commission', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ug_provider = models.CharField(db_column='UG_Provider', max_length=15, blank=True, null=True)  # Field name made lowercase.
    auth_method = models.CharField(db_column='Auth_Method', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_ugmart_transaction'


class BillUser(models.Model):
    radiususerid = models.PositiveIntegerField(db_column='RadiusUserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=150, blank=True, null=True)  # Field name made lowercase.
    billingcity = models.CharField(db_column='BillingCity', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billingzipcode = models.CharField(db_column='BillingZipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    billingcountry = models.CharField(db_column='BillingCountry', max_length=40, blank=True, null=True)  # Field name made lowercase.
    billingphone = models.CharField(db_column='BillingPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billingemail = models.CharField(db_column='BillingEmail', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cardexpirydate = models.DateField(db_column='CardExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cvvnumber = models.CharField(db_column='CvvNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    signupdate = models.DateTimeField(db_column='SignupDate', blank=True, null=True)  # Field name made lowercase.
    isverified = models.IntegerField(db_column='IsVerified', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nextbillingdate = models.DateTimeField(db_column='NextBillingDate', blank=True, null=True)  # Field name made lowercase.
    lastbillingsuccessdate = models.DateTimeField(db_column='LastBillingSuccessDate', blank=True, null=True)  # Field name made lowercase.
    failedattempts = models.IntegerField(db_column='FailedAttempts', blank=True, null=True)  # Field name made lowercase.
    cardupdated = models.IntegerField(db_column='CardUpdated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    lastrechargedate = models.DateTimeField(db_column='LastRechargeDate', blank=True, null=True)  # Field name made lowercase.
    totaltimelimit = models.PositiveIntegerField(db_column='TotalTimeLimit', blank=True, null=True)  # Field name made lowercase.
    totalbandwidthlimit = models.BigIntegerField(db_column='TotalBandwidthLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_user'


class BillVoucher(models.Model):
    voucherbatchid = models.ForeignKey('BillVoucherBatch', models.DO_NOTHING, db_column='VoucherBatchId', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='VoucherCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.IntegerField(db_column='SerialNumber', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    activationdate = models.DateTimeField(db_column='ActivationDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    usedlocationid = models.IntegerField(db_column='UsedLocationId', blank=True, null=True)  # Field name made lowercase.
    dateused = models.DateTimeField(db_column='DateUsed', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    transid = models.CharField(db_column='TransId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_voucher'


class BillVoucherBatch(models.Model):
    voucherbatchname = models.CharField(db_column='VoucherBatchName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    policyid = models.IntegerField(db_column='PolicyId', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    totalcount = models.IntegerField(db_column='TotalCount', blank=True, null=True)  # Field name made lowercase.
    totalusedcount = models.IntegerField(db_column='TotalUsedCount', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_voucher_batch'


class BillVoucherDesign(models.Model):
    designname = models.CharField(db_column='DesignName', max_length=40)  # Field name made lowercase.
    headerstring = models.CharField(db_column='HeaderString', max_length=64, blank=True, null=True)  # Field name made lowercase.
    footerstring = models.CharField(db_column='FooterString', max_length=64, blank=True, null=True)  # Field name made lowercase.
    logofilename = models.CharField(db_column='LogoFileName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bgfilename = models.CharField(db_column='BgFileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    policyrestrictions = models.IntegerField(db_column='PolicyRestrictions', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_voucher_design'


class BillVoucherLocations(models.Model):
    voucherbatchid = models.IntegerField(db_column='VoucherBatchId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_voucher_locations'


class BillWorldpayTempUser(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    secretquestion = models.CharField(db_column='SecretQuestion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    secretanswer = models.CharField(db_column='SecretAnswer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    isrenew = models.IntegerField(db_column='IsRenew', blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_worldpay_temp_user'


class BillWorldpayTransaction(models.Model):
    billuserid = models.PositiveIntegerField(db_column='BillUserId', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    planid = models.PositiveIntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    worldpay_response = models.CharField(db_column='Worldpay_Response', max_length=20, blank=True, null=True)  # Field name made lowercase.
    worldpay_transactionid = models.CharField(db_column='Worldpay_TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranamount = models.CharField(db_column='TranAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transtatus = models.IntegerField(db_column='TranStatus', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_worldpay_transaction'


class CampaignAdSurvey(models.Model):
    locationid = models.IntegerField(db_column='LocationId')  # Field name made lowercase.
    adcampaignid = models.IntegerField(db_column='AdCampaignId')  # Field name made lowercase.
    surveycampaignid = models.IntegerField(db_column='SurveyCampaignId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaign_ad_survey'


class ConfigNotification(models.Model):
    smsenable = models.IntegerField(db_column='SMSEnable', blank=True, null=True)  # Field name made lowercase.
    emailenable = models.IntegerField(db_column='EmailEnable', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'config_notification'


class CrmCategory(models.Model):
    categoryname = models.CharField(db_column='CategoryName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    isvisible = models.IntegerField(db_column='IsVisible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_category'


class CrmDescription(models.Model):
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    resolution = models.TextField(db_column='Resolution', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_description'


class CrmEmailtemplate(models.Model):
    templatename = models.CharField(db_column='TemplateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    createdby = models.PositiveIntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    templatesubject = models.CharField(db_column='TemplateSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_emailtemplate'


class CrmExtattr(models.Model):
    attributename = models.CharField(db_column='AttributeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isvisible = models.IntegerField(db_column='IsVisible', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_extattr'


class CrmExtvalue(models.Model):
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    attributevalue = models.CharField(db_column='AttributeValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    callno = models.IntegerField(db_column='CallNo', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_extvalue'


class CrmNotes(models.Model):
    ticketid = models.PositiveIntegerField(db_column='TicketId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    accountid = models.PositiveIntegerField(db_column='AccountId', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    isreply = models.IntegerField(db_column='IsReply', blank=True, null=True)  # Field name made lowercase.
    createdby = models.PositiveIntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_notes'


class CrmProblemtype(models.Model):
    problemtypename = models.CharField(db_column='ProblemTypeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    problemdescription = models.TextField(db_column='ProblemDescription', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_problemtype'


class CrmResolution(models.Model):
    resolution = models.CharField(db_column='Resolution', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_resolution'


class CrmSmstemplate(models.Model):
    templatename = models.CharField(db_column='TemplateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_smstemplate'


class CrmTemplatecategory(models.Model):
    categoryname = models.CharField(db_column='CategoryName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isvisible = models.IntegerField(db_column='IsVisible', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_templatecategory'


class CrmTicket(models.Model):
    ticketnumber = models.CharField(db_column='TicketNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromemail = models.CharField(db_column='FromEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assignedto = models.PositiveIntegerField(db_column='AssignedTo', blank=True, null=True)  # Field name made lowercase.
    assignedby = models.PositiveIntegerField(db_column='AssignedBy', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateclosed = models.DateTimeField(db_column='DateClosed', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    fixbydate = models.DateTimeField(db_column='FixByDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    dateresolved = models.DateTimeField(db_column='DateResolved', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    problemtypeid = models.IntegerField(db_column='ProblemTypeId', blank=True, null=True)  # Field name made lowercase.
    severityid = models.IntegerField(db_column='SeverityId', blank=True, null=True)  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId', blank=True, null=True)  # Field name made lowercase.
    isescalated = models.IntegerField(db_column='IsEscalated', blank=True, null=True)  # Field name made lowercase.
    statusreason = models.IntegerField(db_column='StatusReason', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    accountid = models.PositiveIntegerField(db_column='AccountId', blank=True, null=True)  # Field name made lowercase.
    resolution = models.TextField(db_column='Resolution', blank=True, null=True)  # Field name made lowercase.
    deferred = models.TextField(db_column='Deferred', blank=True, null=True)  # Field name made lowercase.
    escalationnote = models.TextField(db_column='EscalationNote', blank=True, null=True)  # Field name made lowercase.
    screenshotpath = models.CharField(db_column='ScreenshotPath', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_ticket'


class CrmTicketconfig(models.Model):
    smtpserver = models.CharField(db_column='SmtpServer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ccaddress = models.CharField(db_column='CcAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sendconfirmation = models.IntegerField(db_column='SendConfirmation', blank=True, null=True)  # Field name made lowercase.
    templateid = models.PositiveIntegerField(db_column='TemplateId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    lastticketid = models.IntegerField(db_column='LastTicketId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_ticketconfig'


class CronReports(models.Model):
    reportidentifier = models.CharField(db_column='ReportIdentifier', max_length=45)  # Field name made lowercase.
    lasttimestampscanned = models.DateTimeField(db_column='LastTimestampScanned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cron_reports'


class CustomerBillingPlan(models.Model):
    plantype = models.CharField(db_column='PlanType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    planid = models.AutoField(db_column='PlanId', primary_key=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planprice = models.FloatField(db_column='PlanPrice', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.IntegerField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    validityunit = models.CharField(db_column='ValidityUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    perdayplanprice = models.IntegerField(db_column='PerDayPlanPrice', blank=True, null=True)  # Field name made lowercase.
    plannoofdays = models.IntegerField(db_column='PlanNoOfDays', blank=True, null=True)  # Field name made lowercase.
    featureslist = models.TextField(db_column='FeaturesList')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    plancurrency = models.CharField(db_column='PlanCurrency', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_billing_plan'


class Devicetype(models.Model):
    typename = models.CharField(db_column='TypeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15, blank=True, null=True)  # Field name made lowercase.
    snmpenabled = models.IntegerField(db_column='SnmpEnabled', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    deviceowner = models.CharField(db_column='DeviceOwner', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'devicetype'


class EmailTempCustomer(models.Model):
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=50, blank=True, null=True)  # Field name made lowercase.
    used = models.IntegerField(db_column='Used', blank=True, null=True)  # Field name made lowercase.
    tokenexpiry = models.DateTimeField(db_column='TokenExpiry', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_temp_customer'


class EventLogs(models.Model):
    eventid = models.CharField(db_column='EventId', max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apmacaddress = models.CharField(db_column='ApMacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='EventTime')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    apid = models.IntegerField(db_column='APId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_logs'


class Events(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    severity = models.CharField(db_column='Severity', max_length=8)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=7)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=2)  # Field name made lowercase.
    runningevent = models.CharField(db_column='RunningEvent', max_length=1)  # Field name made lowercase.
    oppositeeventid = models.CharField(db_column='OppositeEventId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    userrelated = models.CharField(db_column='UserRelated', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'


class ExternalUserdata(models.Model):
    uniqueid = models.CharField(db_column='UniqueId', unique=True, max_length=20)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'external_userdata'


class ExtportUrl(models.Model):
    id = models.IntegerField()
    portalurl = models.CharField(db_column='PortalUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oldportalurl = models.CharField(db_column='OldPortalUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extport_url'


class FacebookLike(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    degree = models.CharField(db_column='Degree', max_length=20, blank=True, null=True)  # Field name made lowercase.
    degreeyear = models.CharField(db_column='Degreeyear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hometown = models.CharField(db_column='HomeTown', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userfbid = models.CharField(db_column='UserFbId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=10, blank=True, null=True)  # Field name made lowercase.
    workname = models.CharField(db_column='WorkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='TimeZone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.CharField(db_column='UpdatedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radiususerid = models.PositiveIntegerField(db_column='RadiusUserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facebook_like'


class FacebookPageUser(models.Model):
    pageurl = models.CharField(db_column='PageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    likedate = models.DateTimeField(db_column='LikeDate', blank=True, null=True)  # Field name made lowercase.
    userfbid = models.CharField(db_column='UserFbId', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facebook_page_user'


class FacebookUserinfo(models.Model):
    fbid = models.CharField(db_column='FbId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbname = models.CharField(db_column='FbName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbusername = models.CharField(db_column='FbUserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbgender = models.CharField(db_column='FbGender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbemail = models.CharField(db_column='FbEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbtimezone = models.CharField(db_column='FbTimezone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fblocale = models.CharField(db_column='FbLocale', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbupdatedtime = models.CharField(db_column='FbUpdatedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbminage = models.IntegerField(db_column='FbMinAge', blank=True, null=True)  # Field name made lowercase.
    fbmaxage = models.IntegerField(db_column='FbMaxAge', blank=True, null=True)  # Field name made lowercase.
    fbfriendscount = models.IntegerField(db_column='FbFriendsCount', blank=True, null=True)  # Field name made lowercase.
    fbbirthday = models.CharField(db_column='Fbbirthday', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbwebsite = models.CharField(db_column='FbWebsite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbcollege = models.CharField(db_column='FbCollege', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbemployer = models.CharField(db_column='FbEmployer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbposition = models.CharField(db_column='FbPosition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facebook_userinfo'


class FacebookUserlogin(models.Model):
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facebook_userlogin'


class FirmwareVersion(models.Model):
    version = models.PositiveIntegerField()
    status = models.IntegerField(blank=True, null=True)
    firmwaretype = models.CharField(db_column='firmwareType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    releasenotes = models.TextField(db_column='releaseNotes', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firmware_version'


class Firmwares(models.Model):
    md5sum = models.CharField(max_length=32)
    board = models.CharField(max_length=50)
    version = models.PositiveIntegerField()
    filename = models.TextField()
    filesize = models.CharField(max_length=20)
    modelno = models.IntegerField(db_column='modelNo', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    firmwaretype = models.CharField(db_column='firmwareType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    releasenotes = models.TextField(db_column='releaseNotes', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firmwares'


class FloormapConfig(models.Model):
    floorid = models.AutoField(db_column='Floorid', primary_key=True)  # Field name made lowercase.
    floorname = models.CharField(db_column='Floorname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    floorimagepath = models.CharField(db_column='Floorimagepath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cretedon = models.DateTimeField(db_column='Cretedon')  # Field name made lowercase.
    floorimagewidth = models.FloatField(db_column='Floorimagewidth', blank=True, null=True)  # Field name made lowercase.
    floorimageheight = models.FloatField(db_column='Floorimageheight', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='Updatedon')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'floormap_config'


class GoogleUserinfo(models.Model):
    gid = models.CharField(db_column='GId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gname = models.CharField(db_column='GName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gusername = models.CharField(db_column='GUserName', max_length=400, blank=True, null=True)  # Field name made lowercase.
    gpictureurl = models.CharField(db_column='GPictureURL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    gemailaddress = models.CharField(db_column='GEmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ggender = models.CharField(db_column='GGender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    glocale = models.CharField(db_column='GLocale', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gminage = models.IntegerField(db_column='GMinAge', blank=True, null=True)  # Field name made lowercase.
    gmaxage = models.IntegerField(db_column='GMaxAge', blank=True, null=True)  # Field name made lowercase.
    gbirthday = models.CharField(db_column='GBirthDay', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gcircledcount = models.IntegerField(db_column='GCircledCount', blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'google_userinfo'


class GoogleUserlogin(models.Model):
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'google_userlogin'


class HotspotDefaults(models.Model):
    hotspotname = models.CharField(db_column='HotspotName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    hotspotdisplayname = models.CharField(db_column='HotspotDisplayName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=10, blank=True, null=True)  # Field name made lowercase.
    locationtypeid = models.PositiveIntegerField(db_column='LocationTypeId', blank=True, null=True)  # Field name made lowercase.
    hotspotstatus = models.CharField(db_column='HotspotStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    automacregister = models.IntegerField(db_column='AutoMacRegister', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workinghours = models.CharField(db_column='WorkingHours', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    updatelocation = models.IntegerField(db_column='UpdateLocation', blank=True, null=True)  # Field name made lowercase.
    isbyod = models.IntegerField(db_column='IsBYOD', blank=True, null=True)  # Field name made lowercase.
    byodcount = models.IntegerField(db_column='BYODCount', blank=True, null=True)  # Field name made lowercase.
    byodexpiry = models.IntegerField(db_column='BYODExpiry', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hotspotplanid = models.IntegerField(db_column='HotspotPlanId', blank=True, null=True)  # Field name made lowercase.
    hotspotplanchangedate = models.DateTimeField(db_column='HotspotPlanChangeDate', blank=True, null=True)  # Field name made lowercase.
    plangroupid = models.PositiveIntegerField(db_column='PlanGroupId')  # Field name made lowercase.
    enablehotspot = models.IntegerField(db_column='EnableHotspot', blank=True, null=True)  # Field name made lowercase.
    splashpage = models.CharField(db_column='SplashPage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablessid = models.IntegerField(db_column='EnableSSID', blank=True, null=True)  # Field name made lowercase.
    visiblessid = models.IntegerField(db_column='VisibleSSID', blank=True, null=True)  # Field name made lowercase.
    ssidname = models.CharField(db_column='SSIDName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssidkey = models.CharField(db_column='SSIDKey', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', unique=True, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotspot_defaults'


class InstagramUserinfo(models.Model):
    iid = models.CharField(db_column='IId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iname = models.CharField(db_column='IName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iusername = models.CharField(db_column='IUserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ifollowerscount = models.CharField(db_column='IFollowersCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ifollowingcount = models.CharField(db_column='IFollowingCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imediacount = models.CharField(db_column='IMediaCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipictureurl = models.CharField(db_column='IPictureURL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instagram_userinfo'


class InstagramUserlogin(models.Model):
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instagram_userlogin'


class LdapConfig(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hostaddress = models.CharField(db_column='HostAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authmethod = models.CharField(db_column='AuthMethod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    searchcriteria = models.CharField(db_column='SearchCriteria', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adminusername = models.CharField(db_column='AdminUsername', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adminpassword = models.CharField(db_column='AdminPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    basedn = models.CharField(db_column='Basedn', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    realm = models.CharField(db_column='Realm', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ldapfilter = models.CharField(db_column='LdapFilter', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ldap_config'


class LinkedinUserinfo(models.Model):
    lid = models.CharField(db_column='LId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lusername = models.CharField(db_column='LUserName', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lemailaddress = models.CharField(db_column='LEmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    llocation = models.CharField(db_column='LLocation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lheadline = models.CharField(db_column='LHeadline', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lsummary = models.CharField(db_column='LSummary', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lbirthday = models.DateField(db_column='LBirthday', blank=True, null=True)  # Field name made lowercase.
    lindustry = models.CharField(db_column='LIndustry', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lconnections = models.CharField(db_column='LConnections', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lpositions = models.IntegerField(db_column='LPositions', blank=True, null=True)  # Field name made lowercase.
    lpositiontitle = models.CharField(db_column='LPositiontitle', max_length=250, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    lpictureurl = models.CharField(db_column='LPictureURL', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linkedin_userinfo'


class LinkedinUserlogin(models.Model):
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linkedin_userlogin'


class Location(models.Model):
    locationname = models.CharField(db_column='LocationName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicetypeid = models.PositiveIntegerField(db_column='DeviceTypeId', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=10, blank=True, null=True)  # Field name made lowercase.
    venuetypeid = models.PositiveIntegerField(db_column='VenueTypeId', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='Timezone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotspotenable = models.PositiveIntegerField(db_column='HotspotEnable')  # Field name made lowercase.
    hotspotplanid = models.IntegerField(db_column='HotspotPlanId', blank=True, null=True)  # Field name made lowercase.
    radiusserver1 = models.CharField(db_column='RadiusServer1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radiusserver2 = models.CharField(db_column='RadiusServer2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radiussecret = models.CharField(db_column='RadiusSecret', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radiusnasid = models.CharField(db_column='RadiusNasId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radiusrequestpassword = models.CharField(db_column='RadiusRequestPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uamserver = models.CharField(db_column='UamServer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passthroughurl = models.CharField(db_column='PassthroughUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    macpassword = models.CharField(db_column='MacPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    autologinenable = models.IntegerField(db_column='AutologinEnable', blank=True, null=True)  # Field name made lowercase.
    automacregister = models.IntegerField(db_column='AutoMacRegister', blank=True, null=True)  # Field name made lowercase.
    autologinvalidity = models.IntegerField(db_column='AutoLoginValidity', blank=True, null=True)  # Field name made lowercase.
    autologinvalidityunit = models.IntegerField(db_column='AutoLoginValidityUnit', blank=True, null=True)  # Field name made lowercase.
    hotspotipaddress = models.CharField(db_column='HotspotIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    interiminterval = models.IntegerField(db_column='InterimInterval', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class LocationAccountingSummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_id = models.IntegerField(blank=True, null=True)
    downloadbytes = models.BigIntegerField(blank=True, null=True)
    uploadbytes = models.BigIntegerField(blank=True, null=True)
    sessiontime = models.BigIntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    sessioncount = models.IntegerField(blank=True, null=True)
    summary_date = models.DateTimeField(blank=True, null=True)
    unique_user_login = models.IntegerField(blank=True, null=True)
    device_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_accounting_summary'
        unique_together = (('location_id', 'summary_date', 'customer_id'),)


class Locationtype(models.Model):
    locationtype = models.CharField(db_column='LocationType', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locationtype'


class ModelRange(models.Model):
    modelname = models.CharField(db_column='modelName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    txpower = models.FloatField(blank=True, null=True)
    d1 = models.FloatField(blank=True, null=True)
    d2 = models.FloatField(blank=True, null=True)
    d3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_range'


class NetworkLifeCycle(models.Model):
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId')  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    totalap = models.IntegerField(db_column='TotalAP', blank=True, null=True)  # Field name made lowercase.
    upap = models.IntegerField(db_column='UpAP', blank=True, null=True)  # Field name made lowercase.
    networkuppercentage = models.IntegerField(db_column='NetworkUpPercentage', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'network_life_cycle'


class OuiDb(models.Model):
    macprefix = models.CharField(db_column='MacPrefix', primary_key=True, max_length=8)  # Field name made lowercase.
    macvendor = models.CharField(db_column='MacVendor', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oui_db'


class Policy(models.Model):
    policyname = models.CharField(db_column='PolicyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    validityinterval = models.IntegerField(db_column='ValidityInterval', blank=True, null=True)  # Field name made lowercase.
    validityunit = models.IntegerField(db_column='ValidityUnit', blank=True, null=True)  # Field name made lowercase.
    dailytimequota = models.BigIntegerField(db_column='DailyTimeQuota', blank=True, null=True)  # Field name made lowercase.
    dailytimequotaunit = models.IntegerField(db_column='DailyTimeQuotaUnit')  # Field name made lowercase.
    totaltimequota = models.BigIntegerField(db_column='TotalTimeQuota', blank=True, null=True)  # Field name made lowercase.
    totaltimequotaunit = models.IntegerField(db_column='TotalTimeQuotaUnit')  # Field name made lowercase.
    dailybandwidthquota = models.BigIntegerField(db_column='DailyBandwidthQuota', blank=True, null=True)  # Field name made lowercase.
    dailybandwidthquotaunit = models.IntegerField(db_column='DailyBandwidthQuotaUnit')  # Field name made lowercase.
    totalbandwidthquota = models.BigIntegerField(db_column='TotalBandwidthQuota', blank=True, null=True)  # Field name made lowercase.
    totalbandwidthquotaunit = models.IntegerField(db_column='TotalBandwidthQuotaUnit')  # Field name made lowercase.
    dailysessioncount = models.IntegerField(db_column='DailySessionCount', blank=True, null=True)  # Field name made lowercase.
    sessiontimeout = models.BigIntegerField(db_column='SessionTimeout', blank=True, null=True)  # Field name made lowercase.
    sessiontimeoutunit = models.IntegerField(db_column='SessionTimeoutUnit')  # Field name made lowercase.
    idletimeout = models.BigIntegerField(db_column='IdleTimeout', blank=True, null=True)  # Field name made lowercase.
    idletimeoutunit = models.IntegerField(db_column='IdleTimeoutUnit')  # Field name made lowercase.
    downloadrate = models.BigIntegerField(db_column='DownloadRate', blank=True, null=True)  # Field name made lowercase.
    downloadrateunit = models.IntegerField(db_column='DownloadRateUnit')  # Field name made lowercase.
    uploadrate = models.BigIntegerField(db_column='UploadRate', blank=True, null=True)  # Field name made lowercase.
    uploadrateunit = models.IntegerField(db_column='UploadRateUnit')  # Field name made lowercase.
    concurrencylimit = models.IntegerField(db_column='ConcurrencyLimit', blank=True, null=True)  # Field name made lowercase.
    maxdevicelimit = models.IntegerField(db_column='MaxDeviceLimit', blank=True, null=True)  # Field name made lowercase.
    autorenewal = models.IntegerField(db_column='AutoRenewal', blank=True, null=True)  # Field name made lowercase.
    enablefup = models.IntegerField(db_column='EnableFup', blank=True, null=True)  # Field name made lowercase.
    fupdailybandwidthquota = models.BigIntegerField(db_column='FupDailyBandwidthQuota', blank=True, null=True)  # Field name made lowercase.
    fupdailybandwidthunit = models.IntegerField(db_column='FupDailyBandwidthUnit')  # Field name made lowercase.
    fupdownloadrate = models.BigIntegerField(db_column='FupDownloadRate', blank=True, null=True)  # Field name made lowercase.
    fupdownloadrateunit = models.IntegerField(db_column='FupDownloadRateUnit')  # Field name made lowercase.
    fupuploadrate = models.BigIntegerField(db_column='FupUploadRate', blank=True, null=True)  # Field name made lowercase.
    fupuploadrateunit = models.IntegerField(db_column='FupUploadrateUnit')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedtime = models.DateTimeField(db_column='LastModifiedTime')  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'policy'


class PortUrl(models.Model):
    portalurl = models.CharField(db_column='PortalUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oldportalurl = models.CharField(db_column='OldPortalUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    portal_config = models.ForeignKey('PortalConfig', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_url'


class PortalConfig(models.Model):
    isdefaultconfig = models.IntegerField(db_column='IsDefaultConfig')  # Field name made lowercase.
    apihost = models.CharField(db_column='ApiHost', max_length=255)  # Field name made lowercase.
    apipath = models.CharField(db_column='ApiPath', max_length=255)  # Field name made lowercase.
    customercode = models.IntegerField(db_column='Customercode')  # Field name made lowercase.
    realm = models.CharField(db_column='Realm', max_length=50)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=10)  # Field name made lowercase.
    optionallanguage = models.CharField(db_column='OptionalLanguage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='Locationname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationdisname = models.CharField(db_column='LocationDisName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enableunamepasswd = models.IntegerField(db_column='EnableUnamePasswd', blank=True, null=True)  # Field name made lowercase.
    unamepasswordtitle = models.CharField(db_column='UnamePasswordTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paidenabletnc = models.IntegerField(db_column='PaidEnableTnc', blank=True, null=True)  # Field name made lowercase.
    paidinstructiontext = models.CharField(db_column='PaidInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    paidplangroupid = models.IntegerField(db_column='PaidPlanGroupId', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqfirstname = models.IntegerField(db_column='PaidUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqlastname = models.IntegerField(db_column='PaidUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqemail = models.IntegerField(db_column='PaidUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqhomephone = models.IntegerField(db_column='PaidUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqaddress = models.IntegerField(db_column='PaidUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqcity = models.IntegerField(db_column='PaidUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqstate = models.IntegerField(db_column='PaidUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqzipcode = models.IntegerField(db_column='PaidUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqcountry = models.IntegerField(db_column='PaidUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqgender = models.IntegerField(db_column='PaidUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    enablevoucher = models.IntegerField(db_column='EnableVoucher', blank=True, null=True)  # Field name made lowercase.
    vouchertitle = models.CharField(db_column='VoucherTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    voucherenabletnc = models.IntegerField(db_column='VoucherEnableTnc', blank=True, null=True)  # Field name made lowercase.
    voucherinstructiontext = models.CharField(db_column='VoucherInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqfirstname = models.IntegerField(db_column='VoucherUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqemail = models.IntegerField(db_column='VoucherUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqhomephone = models.IntegerField(db_column='VoucherUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqgender = models.IntegerField(db_column='VoucherUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqage = models.IntegerField(db_column='VoucherUserInfoReqAge', blank=True, null=True)  # Field name made lowercase.
    enableldap = models.IntegerField(db_column='EnableLdap', blank=True, null=True)  # Field name made lowercase.
    ldaptitle = models.CharField(db_column='LdapTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ldapenabletnc = models.IntegerField(db_column='LdapEnableTnc', blank=True, null=True)  # Field name made lowercase.
    ldapinstructiontext = models.CharField(db_column='LdapInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablefreeonclick = models.IntegerField(db_column='EnableFreeOnClick', blank=True, null=True)  # Field name made lowercase.
    freeonclicktitle = models.CharField(db_column='FreeOnClickTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freeonclickenabletnc = models.IntegerField(db_column='FreeOnClickEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freeonclickinstructiontext = models.CharField(db_column='FreeOnClickInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablefreewithuserinfocapture = models.IntegerField(db_column='EnableFreeWithUserInfoCapture', blank=True, null=True)  # Field name made lowercase.
    freeuserinfotitle = models.CharField(db_column='FreeUserInfoTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freeuserinfoenabletnc = models.IntegerField(db_column='FreeUserInfoEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freeuserinfoinstructiontext = models.CharField(db_column='FreeUserInfoInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    freeuserinfoenableextuserauth = models.IntegerField(db_column='FreeUserInfoEnableExtUserAuth', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqfirstname = models.IntegerField(db_column='FreeUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqlastname = models.IntegerField(db_column='FreeUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqemail = models.IntegerField(db_column='FreeUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqhomephone = models.IntegerField(db_column='FreeUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqaddress = models.IntegerField(db_column='FreeUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqcity = models.IntegerField(db_column='FreeUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqstate = models.IntegerField(db_column='FreeUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqzipcode = models.IntegerField(db_column='FreeUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqcountry = models.IntegerField(db_column='FreeUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqgender = models.IntegerField(db_column='FreeUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqgetunamepasswd = models.IntegerField(db_column='FreeUserInfoReqGetUnamePasswd', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqnosignup = models.IntegerField(db_column='FreeUserInfoReqNoSignup', blank=True, null=True)  # Field name made lowercase.
    enablefreewithpassword = models.IntegerField(db_column='EnableFreeWithPassword', blank=True, null=True)  # Field name made lowercase.
    freewithpasswordtitle = models.CharField(db_column='FreeWithPasswordTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freewithpasswordenabletnc = models.IntegerField(db_column='FreeWithPasswordEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freewithpasswordinstructiontext = models.CharField(db_column='FreeWithPasswordInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    freepasswordreqfirstname = models.IntegerField(db_column='FreePasswordReqFirstname', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqlastname = models.IntegerField(db_column='FreePasswordReqLastname', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqemail = models.IntegerField(db_column='FreePasswordReqEmail', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqhomephone = models.IntegerField(db_column='FreePasswordReqHomephone', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqaddress = models.IntegerField(db_column='FreePasswordReqAddress', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqcity = models.IntegerField(db_column='FreePasswordReqCity', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqstate = models.IntegerField(db_column='FreePasswordReqState', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqzipcode = models.IntegerField(db_column='FreePasswordReqZipcode', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqcountry = models.IntegerField(db_column='FreePasswordReqCountry', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqgender = models.IntegerField(db_column='FreePasswordReqGender', blank=True, null=True)  # Field name made lowercase.
    freeaccesspassword = models.CharField(db_column='FreeAccessPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ldappolicyid = models.IntegerField(db_column='LdapPolicyId', blank=True, null=True)  # Field name made lowercase.
    freepolicyid = models.IntegerField(db_column='FreePolicyId', blank=True, null=True)  # Field name made lowercase.
    freedatacapturepolicyid = models.IntegerField(db_column='FreeDataCapturePolicyId', blank=True, null=True)  # Field name made lowercase.
    smspolicyid = models.IntegerField(db_column='SmsPolicyId', blank=True, null=True)  # Field name made lowercase.
    socialpolicyid = models.IntegerField(db_column='SocialPolicyId', blank=True, null=True)  # Field name made lowercase.
    freepasswordpolicyid = models.IntegerField(db_column='FreePasswordPolicyId', blank=True, null=True)  # Field name made lowercase.
    enablesms = models.IntegerField(db_column='EnableSms', blank=True, null=True)  # Field name made lowercase.
    smstitle = models.CharField(db_column='SmsTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    smsenabletnc = models.IntegerField(db_column='SmsEnableTnc', blank=True, null=True)  # Field name made lowercase.
    smsinstructiontext = models.CharField(db_column='SmsInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqfirstname = models.IntegerField(db_column='SmsUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqlastname = models.IntegerField(db_column='SmsUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqemail = models.IntegerField(db_column='SmsUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqhomephone = models.IntegerField(db_column='SmsUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqaddress = models.IntegerField(db_column='SmsUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqcity = models.IntegerField(db_column='SmsUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqstate = models.IntegerField(db_column='SmsUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqzipcode = models.IntegerField(db_column='SmsUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqcountry = models.IntegerField(db_column='SmsUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqgender = models.IntegerField(db_column='SmsUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqage = models.IntegerField(db_column='SmsUserInfoReqAge', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqbirthdate = models.IntegerField(db_column='SmsUserInfoReqBirthdate', blank=True, null=True)  # Field name made lowercase.
    enablesocialmedia = models.IntegerField(db_column='EnableSocialMedia', blank=True, null=True)  # Field name made lowercase.
    socialmediatitle = models.CharField(db_column='SocialMediaTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    socialmediaenabletnc = models.IntegerField(db_column='SocialMediaEnableTnc', blank=True, null=True)  # Field name made lowercase.
    socialmediainstructiontext = models.CharField(db_column='SocialMediaInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablesmfb = models.IntegerField(db_column='EnableSmFb', blank=True, null=True)  # Field name made lowercase.
    fbappid = models.CharField(db_column='FbAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fbappsecret = models.CharField(db_column='FbAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fblikeurl = models.CharField(db_column='FbLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbshareurl = models.CharField(db_column='FbShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmli = models.IntegerField(db_column='EnableSmLi', blank=True, null=True)  # Field name made lowercase.
    liappid = models.CharField(db_column='LiAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    liappsecret = models.CharField(db_column='LiAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lilikeurl = models.CharField(db_column='LiLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lishareurl = models.CharField(db_column='LiShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmtt = models.IntegerField(db_column='EnableSmTt', blank=True, null=True)  # Field name made lowercase.
    ttappid = models.CharField(db_column='TtAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ttappsecret = models.CharField(db_column='TtAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ttlikeurl = models.CharField(db_column='TtLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ttshareurl = models.CharField(db_column='TtShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmgg = models.IntegerField(db_column='EnableSmGg', blank=True, null=True)  # Field name made lowercase.
    ggappid = models.CharField(db_column='GgAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ggappsecret = models.CharField(db_column='GgAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gglikeurl = models.CharField(db_column='GgLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ggshareurl = models.CharField(db_column='GgShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmig = models.IntegerField(db_column='EnableSmIg', blank=True, null=True)  # Field name made lowercase.
    igappid = models.CharField(db_column='IgAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    igappsecret = models.CharField(db_column='IgAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    igfollowurl = models.CharField(db_column='IgFollowUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parameterpassing = models.CharField(max_length=10)
    enablelogincookies = models.IntegerField(db_column='EnableLoginCookies')  # Field name made lowercase.
    devicetype = models.CharField(db_column='Devicetype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='Deviceid', blank=True, null=True)  # Field name made lowercase.
    requestpassword = models.CharField(db_column='RequestPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reqpaidunamepasswd = models.CharField(db_column='ReqPaidUnamePasswd', max_length=150, blank=True, null=True)  # Field name made lowercase.
    socialplan = models.CharField(db_column='SocialPlan', max_length=150, blank=True, null=True)  # Field name made lowercase.
    enableproximitymarketing = models.IntegerField(db_column='EnableProximityMarketing', blank=True, null=True)  # Field name made lowercase.
    enableselfcare = models.IntegerField(db_column='EnableSelfCare', blank=True, null=True)  # Field name made lowercase.
    enableads = models.IntegerField(db_column='EnableAds', blank=True, null=True)  # Field name made lowercase.
    adonclick = models.CharField(db_column='Adonclick', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enablereview = models.IntegerField(db_column='EnableReview', blank=True, null=True)  # Field name made lowercase.
    enablereviewquestion = models.CharField(db_column='EnableReviewQuestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enablesurvey = models.IntegerField(db_column='EnableSurvey', blank=True, null=True)  # Field name made lowercase.
    voucherpassword = models.CharField(db_column='VoucherPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portallogo = models.CharField(db_column='PortalLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    logoanchorlink = models.CharField(db_column='LogoAnchorLink', max_length=150, blank=True, null=True)  # Field name made lowercase.
    applypartnerlogo = models.CharField(db_column='ApplyPartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    partnerlogo = models.CharField(db_column='PartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalpartnerlogo = models.CharField(db_column='PortalPartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    partnerlogoanchorlink = models.CharField(db_column='PartnerLogoAnchorLink', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalframebackgroundcolor = models.CharField(db_column='PortalFrameBackgroundColor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portalfontcolor = models.CharField(db_column='PortalFontColor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    applysiteimage = models.CharField(db_column='ApplySiteImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    siteimagetheme = models.CharField(db_column='SiteImagetheme', max_length=100, blank=True, null=True)  # Field name made lowercase.
    siteimage = models.CharField(db_column='SiteImage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalsiteimage = models.CharField(db_column='PortalSiteImage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    welcomeurl = models.CharField(db_column='WelcomeUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    footer = models.CharField(db_column='Footer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    showsupportnumber = models.CharField(db_column='ShowSupportNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    supportnumber = models.CharField(db_column='SupportNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    allowtemplatetochangeconfig = models.IntegerField(db_column='AllowTemplateToChangeConfig', blank=True, null=True)  # Field name made lowercase.
    istemplate = models.IntegerField(db_column='IsTemplate', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    templateid = models.ForeignKey('TemplatePortalConfig', models.DO_NOTHING, db_column='TemplateId', blank=True, null=True)  # Field name made lowercase.
    tnctext = models.CharField(db_column='TNCText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portal_config'


class ProxmarkAnnouncement(models.Model):
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=200, blank=True, null=True)  # Field name made lowercase.
    logofile = models.CharField(db_column='LogoFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clickcount = models.IntegerField(db_column='ClickCount', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    destinationlink = models.CharField(db_column='DestinationLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.IntegerField(db_column='NotificationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_announcement'


class ProxmarkAnnouncementLocation(models.Model):
    announcementid = models.IntegerField(db_column='AnnouncementId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_announcement_location'


class ProxmarkConfig(models.Model):
    credentialtype = models.IntegerField(db_column='CredentialType', blank=True, null=True)  # Field name made lowercase.
    webapikey = models.CharField(db_column='WebAPIKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    senderid = models.CharField(db_column='SenderId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    welcomelogo = models.CharField(db_column='WelcomeLogo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    welcometitle = models.CharField(db_column='WelcomeTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    welcomemessage = models.CharField(db_column='WelcomeMessage', max_length=300, blank=True, null=True)  # Field name made lowercase.
    onlinetotalcount = models.IntegerField(db_column='OnlineTotalCount', blank=True, null=True)  # Field name made lowercase.
    onlineinternotificationinterval = models.IntegerField(db_column='OnlineInterNotificationInterVal', blank=True, null=True)  # Field name made lowercase.
    offlinetotalcount = models.IntegerField(db_column='OfflineTotalCount', blank=True, null=True)  # Field name made lowercase.
    offlineinternotificationinterval = models.IntegerField(db_column='OfflineInterNotificationInterVal', blank=True, null=True)  # Field name made lowercase.
    offlinetotalrepeatcount = models.IntegerField(db_column='OfflineTotalRepeatCount', blank=True, null=True)  # Field name made lowercase.
    offlinenotificationrepeatinterval = models.IntegerField(db_column='OfflineNotificationRepeatInterVal', blank=True, null=True)  # Field name made lowercase.
    onlinetotalrepeatcount = models.IntegerField(db_column='OnlineTotalRepeatCount', blank=True, null=True)  # Field name made lowercase.
    onlinenotificationrepeatinterval = models.IntegerField(db_column='OnlineNotificationRepeatInterVal', blank=True, null=True)  # Field name made lowercase.
    proximitynotificationflag = models.IntegerField(db_column='ProximityNotificationFlag', blank=True, null=True)  # Field name made lowercase.
    offlinenotificationflag = models.IntegerField(db_column='OfflineNotificationFlag', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    proximitynotificationurl = models.CharField(db_column='ProximityNotificationUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_config'


class ProxmarkFeatureStatus(models.Model):
    macaddress = models.CharField(db_column='MACAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    reqdatetime = models.DateTimeField(db_column='ReqDateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    raduserid = models.IntegerField(db_column='RadUserId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_feature_status'


class ProxmarkNotificationClickHistory(models.Model):
    notificationid = models.PositiveIntegerField(db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.
    subscriberid = models.PositiveIntegerField(db_column='SubscriberId', blank=True, null=True)  # Field name made lowercase.
    clickdatetime = models.DateTimeField(db_column='ClickDateTime', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    sentid = models.IntegerField(db_column='SentId', blank=True, null=True)  # Field name made lowercase.
    schedulerid = models.IntegerField(db_column='SchedulerId', blank=True, null=True)  # Field name made lowercase.
    isonline = models.IntegerField(db_column='IsOnline', blank=True, null=True)  # Field name made lowercase.
    sentdatetime = models.DateTimeField(db_column='SentDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_notification_click_history'


class ProxmarkNotificationReqtrack(models.Model):
    reqid = models.CharField(db_column='ReqId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    schedulerid = models.IntegerField(db_column='SchedulerId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.IntegerField(db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.
    subscriberid = models.PositiveIntegerField(db_column='SubscriberId', blank=True, null=True)  # Field name made lowercase.
    requesttime = models.DateTimeField(db_column='RequestTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_notification_reqtrack'


class ProxmarkNotificationSentHistory(models.Model):
    notificationid = models.PositiveIntegerField(db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.
    subscriberid = models.PositiveIntegerField(db_column='SubscriberId', blank=True, null=True)  # Field name made lowercase.
    sentdatetime = models.DateTimeField(db_column='SentDateTime', blank=True, null=True)  # Field name made lowercase.
    statusmessage = models.CharField(db_column='StatusMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    reqid = models.CharField(db_column='ReqId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    schedulerid = models.IntegerField(db_column='SchedulerId', blank=True, null=True)  # Field name made lowercase.
    isonline = models.IntegerField(db_column='IsOnline', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_notification_sent_history'


class ProxmarkProximityConfigNotification(models.Model):
    notificationid = models.PositiveIntegerField(db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.
    proximityschedulerid = models.PositiveIntegerField(db_column='ProximitySchedulerId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_proximity_config_notification'


class ProxmarkProximityScheduler(models.Model):
    schedulername = models.CharField(db_column='SchedulerName', max_length=70, blank=True, null=True)  # Field name made lowercase.
    enableproximity = models.IntegerField(db_column='EnableProximity', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_proximity_scheduler'


class ProxmarkProximityZone(models.Model):
    zonename = models.CharField(db_column='ZoneName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    accesspointmac = models.CharField(db_column='AccessPointMac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_proximity_zone'


class ProxmarkPushNotification(models.Model):
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=200, blank=True, null=True)  # Field name made lowercase.
    destinationlink = models.CharField(db_column='DestinationLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logofile = models.CharField(db_column='LogoFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    sentcount = models.IntegerField(db_column='SentCount', blank=True, null=True)  # Field name made lowercase.
    clickcount = models.IntegerField(db_column='ClickCount', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    senddays = models.CharField(db_column='SendDays', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sendhours = models.CharField(db_column='SendHours', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enableoffline = models.IntegerField(db_column='EnableOffline', blank=True, null=True)  # Field name made lowercase.
    timeintervalperiod = models.CharField(db_column='TimeIntervalPeriod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    timeintervalunit = models.CharField(db_column='TimeIntervalUnit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    offlinesendhour = models.CharField(db_column='OfflineSendHour', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_push_notification'


class ProxmarkSchedulerHotspot(models.Model):
    proximityschedulerid = models.IntegerField(db_column='ProximitySchedulerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    haszone = models.IntegerField(db_column='HasZone', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_scheduler_hotspot'


class ProxmarkSchedulerZone(models.Model):
    proximityschedulerid = models.PositiveIntegerField(db_column='ProximitySchedulerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_scheduler_zone'


class ProxmarkSubscribers(models.Model):
    token = models.CharField(db_column='Token', max_length=250, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clickcount = models.IntegerField(db_column='ClickCount', blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    raduserid = models.IntegerField(db_column='RadUserId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    subscribedatetime = models.DateTimeField(db_column='SubscribeDateTime')  # Field name made lowercase.
    onlinesentcount = models.IntegerField(db_column='OnlineSentCount', blank=True, null=True)  # Field name made lowercase.
    offlinesentcount = models.IntegerField(db_column='OfflineSentCount', blank=True, null=True)  # Field name made lowercase.
    sentcount = models.IntegerField(db_column='SentCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_subscribers'


class ProxmarkZoneMac(models.Model):
    zoneid = models.ForeignKey(ProxmarkProximityZone, models.DO_NOTHING, db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxmark_zone_mac'


class RogueApClassification(models.Model):
    napmacaddress = models.CharField(db_column='NApMacAddress', unique=True, max_length=20)  # Field name made lowercase.
    lastcheckintime = models.DateTimeField(db_column='LastCheckinTime', blank=True, null=True)  # Field name made lowercase.
    uptime = models.CharField(db_column='Uptime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ssid = models.CharField(db_column='SSID', max_length=33)  # Field name made lowercase.
    frequency = models.SmallIntegerField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    rssi = models.IntegerField(db_column='Rssi', blank=True, null=True)  # Field name made lowercase.
    primarychannel = models.IntegerField(db_column='PrimaryChannel', blank=True, null=True)  # Field name made lowercase.
    secondarychannel = models.IntegerField(db_column='SecondaryChannel', blank=True, null=True)  # Field name made lowercase.
    channelwidth = models.CharField(db_column='ChannelWidth', max_length=8, blank=True, null=True)  # Field name made lowercase.
    stachannelwidth = models.CharField(db_column='StaChannelWidth', max_length=8, blank=True, null=True)  # Field name made lowercase.
    firstcenterfrequency = models.CharField(db_column='FirstCenterFrequency', max_length=8, blank=True, null=True)  # Field name made lowercase.
    secondcenterfrequency = models.CharField(db_column='SecondCenterFrequency', max_length=8, blank=True, null=True)  # Field name made lowercase.
    authentication = models.CharField(db_column='Authentication', max_length=20, blank=True, null=True)  # Field name made lowercase.
    security = models.CharField(db_column='Security', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    enablerogue = models.CharField(db_column='EnableRogue', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rogue_ap_classification'
        unique_together = (('id', 'napmacaddress'),)


class SendEmailAlertsNotifications(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.PositiveIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fromemailid = models.CharField(db_column='FromEmailId', max_length=20)  # Field name made lowercase.
    toemailid = models.CharField(db_column='ToEmailId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    templatesubject = models.CharField(db_column='TemplateSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.
    callingstationid = models.CharField(db_column='CallingStationId', max_length=30)  # Field name made lowercase.
    authdatetimestamp = models.DateTimeField(db_column='AuthDateTimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'send_email_alerts_notifications'


class SendSmsAlertsNotifications(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.PositiveIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    smscontent = models.CharField(db_column='SMSContent', max_length=200)  # Field name made lowercase.
    message_entry = models.CharField(db_column='Message_entry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    callingstationid = models.CharField(db_column='CallingStationId', max_length=30)  # Field name made lowercase.
    authdatetimestamp = models.DateTimeField(db_column='AuthDateTimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'send_sms_alerts_notifications'


class SignupTempCustomer(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=50, blank=True, null=True)  # Field name made lowercase.
    used = models.IntegerField(db_column='Used', blank=True, null=True)  # Field name made lowercase.
    tokenexpiry = models.DateTimeField(db_column='TokenExpiry', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    countryid = models.CharField(db_column='CountryId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timezonename = models.CharField(db_column='TimezoneName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    companyshortname = models.CharField(db_column='CompanyShortName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signup_temp_customer'


class SmartContent(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.
    contenttype = models.IntegerField(db_column='ContentType', blank=True, null=True)  # Field name made lowercase.
    contentsize = models.CharField(db_column='ContentSize', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'smart_content'


class SmsDetails(models.Model):
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    authdatetimestamp = models.DateTimeField(db_column='AuthDateTimeStamp')  # Field name made lowercase.
    callingstationid = models.CharField(db_column='CallingStationId', max_length=30)  # Field name made lowercase.
    smscontent = models.CharField(db_column='SMSContent', max_length=200)  # Field name made lowercase.
    verificationcode = models.CharField(db_column='VerificationCode', max_length=50)  # Field name made lowercase.
    message_entry = models.CharField(db_column='Message_entry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='IsUsed', blank=True, null=True)  # Field name made lowercase.
    smsattemptcount = models.IntegerField(db_column='SMSAttemptCount', blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    otpexpirydate = models.DateTimeField(db_column='OTPExpiryDate', blank=True, null=True)  # Field name made lowercase.
    locationid = models.PositiveIntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.PositiveIntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_details'


class SmsGateway(models.Model):
    gatewaytypeid = models.PositiveIntegerField(db_column='GatewayTypeId', blank=True, null=True)  # Field name made lowercase.
    apiusername = models.CharField(db_column='APIUserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apipassword = models.CharField(db_column='APIPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    twilionumber = models.CharField(db_column='TwilioNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apiid = models.CharField(db_column='ApiId', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sourceaddress = models.CharField(db_column='SourceAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalattemptstosendsms = models.IntegerField(db_column='TotalAttemptsToSendSMS', blank=True, null=True)  # Field name made lowercase.
    smstemplate = models.CharField(db_column='SMSTemplate', max_length=300, blank=True, null=True)  # Field name made lowercase.
    validityinterval = models.IntegerField(db_column='ValidityInterval', blank=True, null=True)  # Field name made lowercase.
    validityunit = models.IntegerField(db_column='ValidityUnit', blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='Route', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    currentbalance = models.PositiveIntegerField(db_column='CurrentBalance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_gateway'


class SmsGatewaytype(models.Model):
    gatewayname = models.CharField(db_column='GatewayName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    gatewayurl = models.CharField(db_column='GatewayUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smsbalanceurl = models.CharField(db_column='SMSBalanceURL', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_gatewaytype'


class SmsTemplate(models.Model):
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_template'


class SnapshotOnlineUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    online = models.BigIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(AdmCustomer, models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snapshot_online_user'


class SocialMediaUserActions(models.Model):
    logintype = models.CharField(db_column='LoginType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    useraction = models.CharField(db_column='UserAction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_media_user_actions'


class SubscriptionGateway(models.Model):
    gatewaytypeid = models.PositiveIntegerField(db_column='GatewayTypeId', blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    testmode = models.IntegerField(db_column='TestMode', blank=True, null=True)  # Field name made lowercase.
    paypalusername = models.CharField(db_column='PaypalUserName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    redirectserverip = models.CharField(db_column='RedirectServerIp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encryptionkey = models.CharField(db_column='EncryptionKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isenabled = models.IntegerField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_gateway'


class SubscriptionInformation(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    planprice = models.IntegerField(db_column='PlanPrice', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiodexpirydate = models.DateTimeField(db_column='GracePeriodExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.IntegerField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    plantype = models.CharField(db_column='PlanType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    activeplanflag = models.IntegerField(db_column='ActivePlanFlag', blank=True, null=True)  # Field name made lowercase.
    lastrechargeaddeddaysincurrentplan = models.IntegerField(db_column='LastRechargeAddedDaysInCurrentPlan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_information'


class SubscriptionInformationTemp(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiodexpirydate = models.DateTimeField(db_column='GracePeriodExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.IntegerField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    plantype = models.CharField(db_column='PlanType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_information_temp'


class SubscriptionPaymentGatewayTemp(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planprice = models.CharField(db_column='PlanPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planstartdate = models.DateTimeField(db_column='PlanStartDate', blank=True, null=True)  # Field name made lowercase.
    planexpirydate = models.DateTimeField(db_column='PlanExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiodexpirydate = models.DateTimeField(db_column='GracePeriodExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.IntegerField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    lastrechargedaysremains = models.IntegerField(db_column='LastRechargeDaysRemains', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentgatewaytypeid = models.IntegerField(db_column='PaymentGatewayTypeId', blank=True, null=True)  # Field name made lowercase.
    paymentgatewayname = models.CharField(db_column='PaymentGatewayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentgatewaycurrencycode = models.CharField(db_column='PaymentGatewayCurrencyCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plantype = models.CharField(db_column='PlanType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_payment_gateway_temp'


class SubscriptionPaymentGatewayTransaction(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planprice = models.CharField(db_column='PlanPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    planstartdate = models.DateTimeField(db_column='PlanStartDate', blank=True, null=True)  # Field name made lowercase.
    planexpirydate = models.DateTimeField(db_column='PlanExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiodexpirydate = models.DateTimeField(db_column='GracePeriodExpiryDate', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.IntegerField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    lastrechargedaysremains = models.IntegerField(db_column='LastRechargeDaysRemains', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentgatewaytypeid = models.IntegerField(db_column='PaymentGatewayTypeId', blank=True, null=True)  # Field name made lowercase.
    paymentgatewayname = models.CharField(db_column='PaymentGatewayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentgatewaycurrencycode = models.CharField(db_column='PaymentGatewayCurrencyCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactionstatus = models.CharField(db_column='TransactionStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactionreturncode = models.CharField(db_column='TransactionReturnCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactionreturnmessage = models.CharField(db_column='TransactionReturnMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transactionamount = models.CharField(db_column='TransactionAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    plantype = models.CharField(db_column='PlanType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_payment_gateway_transaction'


class SurveyCampaign(models.Model):
    campaignname = models.CharField(db_column='CampaignName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    enablealllocation = models.IntegerField(db_column='EnableAllLocation', blank=True, null=True)  # Field name made lowercase.
    displayhours = models.CharField(db_column='DisplayHours', max_length=24, blank=True, null=True)  # Field name made lowercase.
    displaydays = models.CharField(db_column='DisplayDays', max_length=7, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_campaign'


class SurveyCampaignLocation(models.Model):
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.ForeignKey(SurveyCampaign, models.DO_NOTHING, db_column='CampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_campaign_location'


class SurveyCampaignSurveygroup(models.Model):
    surveyid = models.IntegerField(db_column='SurveyId', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.ForeignKey(SurveyCampaign, models.DO_NOTHING, db_column='CampaignId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_campaign_surveygroup'


class SurveyCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_category'


class SurveyGroup(models.Model):
    surveyname = models.CharField(db_column='SurveyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.
    isrepeatablenetwork = models.IntegerField(db_column='IsRepeatableNetwork', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_group'


class SurveyGroupQuestionMapping(models.Model):
    surveyid = models.ForeignKey(SurveyGroup, models.DO_NOTHING, db_column='SurveyId', blank=True, null=True)  # Field name made lowercase.
    questionid = models.ForeignKey('SurveyQuestionnaire', models.DO_NOTHING, db_column='QuestionId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_group_question_mapping'


class SurveyOption(models.Model):
    qid = models.ForeignKey('SurveyQuestionnaire', models.DO_NOTHING, db_column='qid')
    options = models.CharField(db_column='Options', max_length=400, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_option'


class SurveyQuestionAnswer(models.Model):
    usermac = models.CharField(db_column='UserMac', max_length=30, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campaignid = models.IntegerField(db_column='CampaignId', blank=True, null=True)  # Field name made lowercase.
    surveyid = models.IntegerField(db_column='SurveyId', blank=True, null=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionId', blank=True, null=True)  # Field name made lowercase.
    option = models.CharField(db_column='Option', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.
    isskip = models.IntegerField(db_column='IsSkip', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_question_answer'


class SurveyQuestionnaire(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=300, blank=True, null=True)  # Field name made lowercase.
    optiontype = models.CharField(db_column='OptionType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey_questionnaire'


class TemplatePortalConfig(models.Model):
    templatename = models.CharField(db_column='TemplateName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isdefaultconfig = models.IntegerField(db_column='IsDefaultConfig')  # Field name made lowercase.
    apihost = models.CharField(db_column='ApiHost', max_length=255)  # Field name made lowercase.
    apipath = models.CharField(db_column='ApiPath', max_length=255)  # Field name made lowercase.
    customercode = models.IntegerField(db_column='Customercode')  # Field name made lowercase.
    realm = models.CharField(db_column='Realm', max_length=50)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=10)  # Field name made lowercase.
    optionallanguage = models.CharField(db_column='OptionalLanguage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='Locationname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enableunamepasswd = models.IntegerField(db_column='EnableUnamePasswd', blank=True, null=True)  # Field name made lowercase.
    unamepasswordtitle = models.CharField(db_column='UnamePasswordTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paidenabletnc = models.IntegerField(db_column='PaidEnableTnc', blank=True, null=True)  # Field name made lowercase.
    paidinstructiontext = models.CharField(db_column='PaidInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    paidplangroupid = models.IntegerField(db_column='PaidPlanGroupId', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqfirstname = models.IntegerField(db_column='PaidUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqlastname = models.IntegerField(db_column='PaidUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqemail = models.IntegerField(db_column='PaidUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqhomephone = models.IntegerField(db_column='PaidUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqaddress = models.IntegerField(db_column='PaidUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqcity = models.IntegerField(db_column='PaidUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqstate = models.IntegerField(db_column='PaidUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqzipcode = models.IntegerField(db_column='PaidUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqcountry = models.IntegerField(db_column='PaidUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    paiduserinforeqgender = models.IntegerField(db_column='PaidUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    enablevoucher = models.IntegerField(db_column='EnableVoucher', blank=True, null=True)  # Field name made lowercase.
    vouchertitle = models.CharField(db_column='VoucherTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    voucherenabletnc = models.IntegerField(db_column='VoucherEnableTnc', blank=True, null=True)  # Field name made lowercase.
    voucherinstructiontext = models.CharField(db_column='VoucherInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqfirstname = models.IntegerField(db_column='VoucherUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqemail = models.IntegerField(db_column='VoucherUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqhomephone = models.IntegerField(db_column='VoucherUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqgender = models.IntegerField(db_column='VoucherUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    voucheruserinforeqage = models.IntegerField(db_column='VoucherUserInfoReqAge', blank=True, null=True)  # Field name made lowercase.
    enableldap = models.IntegerField(db_column='EnableLdap', blank=True, null=True)  # Field name made lowercase.
    ldaptitle = models.CharField(db_column='LdapTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ldapenabletnc = models.IntegerField(db_column='LdapEnableTnc', blank=True, null=True)  # Field name made lowercase.
    ldapinstructiontext = models.CharField(db_column='LdapInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablefreeonclick = models.IntegerField(db_column='EnableFreeOnClick', blank=True, null=True)  # Field name made lowercase.
    freeonclicktitle = models.CharField(db_column='FreeOnClickTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freeonclickenabletnc = models.IntegerField(db_column='FreeOnClickEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freeonclickinstructiontext = models.CharField(db_column='FreeOnClickInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablefreewithuserinfocapture = models.IntegerField(db_column='EnableFreeWithUserInfoCapture', blank=True, null=True)  # Field name made lowercase.
    freeuserinfotitle = models.CharField(db_column='FreeUserInfoTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freeuserinfoenabletnc = models.IntegerField(db_column='FreeUserInfoEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freeuserinfoinstructiontext = models.CharField(db_column='FreeUserInfoInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    freeuserinfoenableextuserauth = models.IntegerField(db_column='FreeUserInfoEnableExtUserAuth', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqfirstname = models.IntegerField(db_column='FreeUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqlastname = models.IntegerField(db_column='FreeUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqemail = models.IntegerField(db_column='FreeUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqhomephone = models.IntegerField(db_column='FreeUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqaddress = models.IntegerField(db_column='FreeUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqcity = models.IntegerField(db_column='FreeUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqstate = models.IntegerField(db_column='FreeUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqzipcode = models.IntegerField(db_column='FreeUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqcountry = models.IntegerField(db_column='FreeUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqgender = models.IntegerField(db_column='FreeUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqgetunamepasswd = models.IntegerField(db_column='FreeUserInfoReqGetUnamePasswd', blank=True, null=True)  # Field name made lowercase.
    freeuserinforeqnosignup = models.IntegerField(db_column='FreeUserInfoReqNoSignup', blank=True, null=True)  # Field name made lowercase.
    enablefreewithpassword = models.IntegerField(db_column='EnableFreeWithPassword', blank=True, null=True)  # Field name made lowercase.
    freewithpasswordtitle = models.CharField(db_column='FreeWithPasswordTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    freewithpasswordenabletnc = models.IntegerField(db_column='FreeWithPasswordEnableTnc', blank=True, null=True)  # Field name made lowercase.
    freewithpasswordinstructiontext = models.CharField(db_column='FreeWithPasswordInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    freepasswordreqfirstname = models.IntegerField(db_column='FreePasswordReqFirstname', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqlastname = models.IntegerField(db_column='FreePasswordReqLastname', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqemail = models.IntegerField(db_column='FreePasswordReqEmail', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqhomephone = models.IntegerField(db_column='FreePasswordReqHomephone', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqaddress = models.IntegerField(db_column='FreePasswordReqAddress', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqcity = models.IntegerField(db_column='FreePasswordReqCity', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqstate = models.IntegerField(db_column='FreePasswordReqState', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqzipcode = models.IntegerField(db_column='FreePasswordReqZipcode', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqcountry = models.IntegerField(db_column='FreePasswordReqCountry', blank=True, null=True)  # Field name made lowercase.
    freepasswordreqgender = models.IntegerField(db_column='FreePasswordReqGender', blank=True, null=True)  # Field name made lowercase.
    freeaccesspassword = models.CharField(db_column='FreeAccessPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ldappolicyid = models.IntegerField(db_column='LdapPolicyId', blank=True, null=True)  # Field name made lowercase.
    freepolicyid = models.IntegerField(db_column='FreePolicyId', blank=True, null=True)  # Field name made lowercase.
    freedatacapturepolicyid = models.IntegerField(db_column='FreeDataCapturePolicyId', blank=True, null=True)  # Field name made lowercase.
    smspolicyid = models.IntegerField(db_column='SmsPolicyId', blank=True, null=True)  # Field name made lowercase.
    socialpolicyid = models.IntegerField(db_column='SocialPolicyId', blank=True, null=True)  # Field name made lowercase.
    freepasswordpolicyid = models.IntegerField(db_column='FreePasswordPolicyId', blank=True, null=True)  # Field name made lowercase.
    enablesms = models.IntegerField(db_column='EnableSms', blank=True, null=True)  # Field name made lowercase.
    smstitle = models.CharField(db_column='SmsTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    smsenabletnc = models.IntegerField(db_column='SmsEnableTnc', blank=True, null=True)  # Field name made lowercase.
    smsinstructiontext = models.CharField(db_column='SmsInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqfirstname = models.IntegerField(db_column='SmsUserInfoReqFirstname', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqlastname = models.IntegerField(db_column='SmsUserInfoReqLastname', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqemail = models.IntegerField(db_column='SmsUserInfoReqEmail', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqhomephone = models.IntegerField(db_column='SmsUserInfoReqHomephone', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqaddress = models.IntegerField(db_column='SmsUserInfoReqAddress', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqcity = models.IntegerField(db_column='SmsUserInfoReqCity', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqstate = models.IntegerField(db_column='SmsUserInfoReqState', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqzipcode = models.IntegerField(db_column='SmsUserInfoReqZipcode', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqcountry = models.IntegerField(db_column='SmsUserInfoReqCountry', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqgender = models.IntegerField(db_column='SmsUserInfoReqGender', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqage = models.IntegerField(db_column='SmsUserInfoReqAge', blank=True, null=True)  # Field name made lowercase.
    smsuserinforeqbirthdate = models.IntegerField(db_column='SmsUserInfoReqBirthdate', blank=True, null=True)  # Field name made lowercase.
    enablesocialmedia = models.IntegerField(db_column='EnableSocialMedia', blank=True, null=True)  # Field name made lowercase.
    socialmediatitle = models.CharField(db_column='SocialMediaTitle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    socialmediaenabletnc = models.IntegerField(db_column='SocialMediaEnableTnc', blank=True, null=True)  # Field name made lowercase.
    socialmediainstructiontext = models.CharField(db_column='SocialMediaInstructionText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enablesmfb = models.IntegerField(db_column='EnableSmFb', blank=True, null=True)  # Field name made lowercase.
    fbappid = models.CharField(db_column='FbAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fbappsecret = models.CharField(db_column='FbAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fblikeurl = models.CharField(db_column='FbLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbshareurl = models.CharField(db_column='FbShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmli = models.IntegerField(db_column='EnableSmLi', blank=True, null=True)  # Field name made lowercase.
    liappid = models.CharField(db_column='LiAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    liappsecret = models.CharField(db_column='LiAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lilikeurl = models.CharField(db_column='LiLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lishareurl = models.CharField(db_column='LiShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmtt = models.IntegerField(db_column='EnableSmTt', blank=True, null=True)  # Field name made lowercase.
    ttappid = models.CharField(db_column='TtAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ttappsecret = models.CharField(db_column='TtAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ttlikeurl = models.CharField(db_column='TtLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ttshareurl = models.CharField(db_column='TtShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmgg = models.IntegerField(db_column='EnableSmGg', blank=True, null=True)  # Field name made lowercase.
    ggappid = models.CharField(db_column='GgAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ggappsecret = models.CharField(db_column='GgAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gglikeurl = models.CharField(db_column='GgLikeUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ggshareurl = models.CharField(db_column='GgShareUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablesmig = models.IntegerField(db_column='EnableSmIg', blank=True, null=True)  # Field name made lowercase.
    igappid = models.CharField(db_column='IgAppId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    igappsecret = models.CharField(db_column='IgAppSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.
    igfollowurl = models.CharField(db_column='IgFollowUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parameterpassing = models.CharField(max_length=10)
    enablelogincookies = models.IntegerField(db_column='EnableLoginCookies')  # Field name made lowercase.
    devicetype = models.CharField(db_column='Devicetype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='Deviceid', blank=True, null=True)  # Field name made lowercase.
    requestpassword = models.CharField(db_column='RequestPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reqpaidunamepasswd = models.CharField(db_column='ReqPaidUnamePasswd', max_length=150, blank=True, null=True)  # Field name made lowercase.
    socialplan = models.CharField(db_column='SocialPlan', max_length=150, blank=True, null=True)  # Field name made lowercase.
    enableproximitymarketing = models.IntegerField(db_column='EnableProximityMarketing', blank=True, null=True)  # Field name made lowercase.
    enableselfcare = models.IntegerField(db_column='EnableSelfCare', blank=True, null=True)  # Field name made lowercase.
    enableads = models.IntegerField(db_column='EnableAds', blank=True, null=True)  # Field name made lowercase.
    adonclick = models.CharField(db_column='Adonclick', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enablereview = models.IntegerField(db_column='EnableReview', blank=True, null=True)  # Field name made lowercase.
    enablereviewquestion = models.CharField(db_column='EnableReviewQuestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enablesurvey = models.IntegerField(db_column='EnableSurvey', blank=True, null=True)  # Field name made lowercase.
    voucherpassword = models.CharField(db_column='VoucherPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portallogo = models.CharField(db_column='PortalLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    logoanchorlink = models.CharField(db_column='LogoAnchorLink', max_length=150, blank=True, null=True)  # Field name made lowercase.
    applypartnerlogo = models.CharField(db_column='ApplyPartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    partnerlogo = models.CharField(db_column='PartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalpartnerlogo = models.CharField(db_column='PortalPartnerLogo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    partnerlogoanchorlink = models.CharField(db_column='PartnerLogoAnchorLink', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalframebackgroundcolor = models.CharField(db_column='PortalFrameBackgroundColor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portalfontcolor = models.CharField(db_column='PortalFontColor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    applysiteimage = models.CharField(db_column='ApplySiteImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    siteimagetheme = models.CharField(db_column='SiteImagetheme', max_length=100, blank=True, null=True)  # Field name made lowercase.
    siteimage = models.CharField(db_column='SiteImage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    portalsiteimage = models.CharField(db_column='PortalSiteImage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    welcomeurl = models.CharField(db_column='WelcomeUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    footer = models.CharField(db_column='Footer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    showsupportnumber = models.CharField(db_column='ShowSupportNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    supportnumber = models.CharField(db_column='SupportNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    restrictlocation = models.IntegerField(db_column='RestrictLocation', blank=True, null=True)  # Field name made lowercase.
    tnctext = models.CharField(db_column='TNCText', max_length=350, blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'template_portal_config'


class TwitterUserinfo(models.Model):
    tid = models.CharField(db_column='TId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tname = models.CharField(db_column='TName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tscreenname = models.CharField(db_column='TScreenName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tfollowerscount = models.CharField(db_column='TFollowersCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tfollowingcount = models.CharField(db_column='TFollowingCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tfavouritescount = models.CharField(db_column='TFavouritesCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tstatusescount = models.CharField(db_column='TStatusesCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tpictureurl = models.CharField(db_column='TPictureURL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tlocation = models.CharField(db_column='TLocation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'twitter_userinfo'


class TwitterUserlogin(models.Model):
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'twitter_userlogin'


class UserPortalReview(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=255, blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='Review', max_length=255, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_portal_review'


class UserTransactions(models.Model):
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    vouchercode = models.CharField(db_column='VoucherCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    voucherbatchid = models.IntegerField(db_column='VoucherBatchId', blank=True, null=True)  # Field name made lowercase.
    transactionamount = models.CharField(db_column='TransactionAmount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    paymentgatewayname = models.CharField(db_column='PaymentGatewayName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionId', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_transactions'


class Useragent(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    useripaddress = models.CharField(db_column='UserIpAddress', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=17, blank=True, null=True)  # Field name made lowercase.
    useragent = models.CharField(db_column='UserAgent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    browsermajor = models.CharField(db_column='BrowserMajor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    browsername = models.CharField(db_column='BrowserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    browserversion = models.CharField(db_column='BrowserVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enginename = models.CharField(db_column='EngineName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    engineversion = models.CharField(db_column='EngineVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osname = models.CharField(db_column='OSName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OSVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicemodel = models.CharField(db_column='DeviceModel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicevendor = models.CharField(db_column='DeviceVendor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpuarchitecture = models.CharField(db_column='CPUArchitecture', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginstatus = models.IntegerField(db_column='LoginStatus', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AdmCustomer, models.DO_NOTHING, db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    logdate = models.DateTimeField(db_column='LogDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useragent'


class VwAdCampaignmap(models.Model):
    campaignid = models.IntegerField(db_column='CampaignId')  # Field name made lowercase.
    campaignweight = models.IntegerField(db_column='CampaignWeight')  # Field name made lowercase.
    adid = models.IntegerField(db_column='AdId')  # Field name made lowercase.
    admediaid = models.IntegerField(db_column='AdMediaId')  # Field name made lowercase.
    destinationlink = models.IntegerField(db_column='DestinationLink')  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight')  # Field name made lowercase.
    totalimpressions = models.IntegerField(db_column='TotalImpressions')  # Field name made lowercase.
    displaydays = models.IntegerField(db_column='DisplayDays')  # Field name made lowercase.
    displayhours = models.IntegerField(db_column='DisplayHours')  # Field name made lowercase.
    adtype = models.IntegerField(db_column='AdType')  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ad_campaignmap'


class VwAdMedia(models.Model):
    id = models.IntegerField()
    image1 = models.IntegerField(db_column='Image1')  # Field name made lowercase.
    imagesize1 = models.IntegerField(db_column='ImageSize1')  # Field name made lowercase.
    imagedimension1 = models.IntegerField(db_column='ImageDimension1')  # Field name made lowercase.
    imagetype1 = models.IntegerField(db_column='ImageType1')  # Field name made lowercase.
    image2 = models.IntegerField(db_column='Image2')  # Field name made lowercase.
    imagesize2 = models.IntegerField(db_column='ImageSize2')  # Field name made lowercase.
    imagedimension2 = models.IntegerField(db_column='ImageDimension2')  # Field name made lowercase.
    imagetype2 = models.IntegerField(db_column='ImageType2')  # Field name made lowercase.
    image3 = models.IntegerField(db_column='Image3')  # Field name made lowercase.
    imagesize3 = models.IntegerField(db_column='ImageSize3')  # Field name made lowercase.
    imagedimension3 = models.IntegerField(db_column='ImageDimension3')  # Field name made lowercase.
    imagetype3 = models.IntegerField(db_column='ImageType3')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    videoname = models.IntegerField(db_column='VideoName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ad_media'


class VwAdStatistics(models.Model):
    admediaid = models.IntegerField(db_column='AdMediaId')  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ad_statistics'


class WifiCountrywiseFrequency(models.Model):
    country = models.CharField(db_column='Country', max_length=50)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3)  # Field name made lowercase.
    channelid = models.ForeignKey('WifiFrequencyBands', models.DO_NOTHING, db_column='ChannelId')  # Field name made lowercase.
    txpower = models.IntegerField(db_column='TxPower', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wifi_countrywise_frequency'


class WifiFrequencyBands(models.Model):
    band = models.IntegerField(db_column='Band')  # Field name made lowercase.
    frequency = models.IntegerField(db_column='Frequency')  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel')  # Field name made lowercase.
    bandwidth = models.IntegerField(db_column='Bandwidth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wifi_frequency_bands'
