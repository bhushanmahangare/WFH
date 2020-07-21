from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import datetime

# User Define packages
from helper import enums

class AdmCustomer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    currency = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    customer_type = models.CharField(max_length=20, choices=[(ctype.value, ctype.name) for ctype in enums.CustomerTypes])
    signup_date = models.DateTimeField(auto_now_add=True)
    prefix = models.CharField(max_length=20, null=True, blank=True)
    customer_code = models.CharField(max_length=20, null=True, blank=True)
    realm = models.CharField(max_length=20, null=True, blank=True)
    logo_url = models.CharField(max_length=450, null=True, blank=True)
    logo_path = models.CharField(max_length=450, null=True, blank=True)
    home_page_url = models.CharField(max_length=450, null=True, blank=True)
    time_zone = models.CharField(max_length=20, null=True, blank=True)
    time_zone_name = models.CharField(max_length=50, null=True, blank=True)
    google_map_key = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = "adm_customer"

    def __str__(self):
        return self.name


class AdmAccount(AbstractUser):

    role = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    customer = models.ForeignKey(
            AdmCustomer,
            on_delete=models.CASCADE
        )

    class Meta:
        db_table = "adm_account"

    def __str__(self):
        return self.username