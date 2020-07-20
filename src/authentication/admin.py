from django.contrib import admin
from authentication.models import AdmCustomer , AdmAccount

admin.site.register(AdmCustomer)
admin.site.register(AdmAccount)