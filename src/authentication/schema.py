# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from authentication.models import AdmCustomer, AdmAccount

class AdmCustomerType(DjangoObjectType):
    class Meta:
        model = AdmCustomer

class AdmAccountType(DjangoObjectType):
    class Meta:
        model = AdmAccount

class Query(object):
    all_customers = graphene.List(AdmCustomerType)
    all_accounts = graphene.List(AdmAccountType)

    def resolve_all_customers(self, info, **kwargs):
        return AdmCustomer.objects.all()
    
    def resolve_all_accounts(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return AdmAccount.objects.select_related('admcustomer').all()
    