# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdmAccount(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254, blank=True, null=True)
    customer = models.ForeignKey('AdmCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adm_account'


class AdmAccountGroups(models.Model):
    admaccount = models.ForeignKey(AdmAccount, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adm_account_groups'
        unique_together = (('admaccount', 'group'),)


class AdmAccountUserPermissions(models.Model):
    admaccount = models.ForeignKey(AdmAccount, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adm_account_user_permissions'
        unique_together = (('admaccount', 'permission'),)


class AdmCustomer(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    customer_type = models.CharField(max_length=20)
    signup_date = models.DateTimeField()
    prefix = models.CharField(max_length=20, blank=True, null=True)
    customer_code = models.CharField(max_length=20, blank=True, null=True)
    realm = models.CharField(max_length=20, blank=True, null=True)
    logo_url = models.CharField(max_length=450, blank=True, null=True)
    logo_path = models.CharField(max_length=450, blank=True, null=True)
    home_page_url = models.CharField(max_length=450, blank=True, null=True)
    time_zone = models.CharField(max_length=20, blank=True, null=True)
    time_zone_name = models.CharField(max_length=50, blank=True, null=True)
    google_map_key = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_customer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AdmAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    locationname = models.CharField(db_column='LocationName', max_length=100)  # Field name made lowercase.
    hotspotenable = models.IntegerField(db_column='HotspotEnable', blank=True, null=True)  # Field name made lowercase.
    autologinenable = models.IntegerField(db_column='AutologinEnable', blank=True, null=True)  # Field name made lowercase.
    automacregister = models.IntegerField(db_column='AutoMacRegister', blank=True, null=True)  # Field name made lowercase.
    autologinvalidity = models.PositiveIntegerField(db_column='AutoLoginValidity', blank=True, null=True)  # Field name made lowercase.
    autologinvalidityunit = models.PositiveSmallIntegerField(db_column='AutoLoginValidityUnit', blank=True, null=True)  # Field name made lowercase.
    interiminterval = models.PositiveSmallIntegerField(db_column='InterimInterval')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'
