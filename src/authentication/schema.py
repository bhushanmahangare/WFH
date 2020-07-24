# cookbook/ingredients/schema.py
import graphene
import logging

from graphene_django.types import DjangoObjectType

from authentication.models import AdmCustomer, AdmAccount

logger = logging.getLogger(__name__)


class AdmCustomerType(DjangoObjectType):
    class Meta:
        model = AdmCustomer

class AdmAccountType(DjangoObjectType):
    class Meta:
        model = AdmAccount

class Query(object):

    #Getting single objects
    customer = graphene.Field(
        AdmCustomerType,
        id=graphene.Int(),
        name=graphene.String()
    )
    #Getting list objects
    all_customers = graphene.List(AdmCustomerType)


    account = graphene.Field(
        AdmAccountType,
        id=graphene.Int(),
        name=graphene.String()
    )
    #Getting list object
    all_accounts = graphene.List(AdmAccountType)


    def resolve_all_customers(self, info, **kwargs):
        logger.debug(f'Resolve all customer funtion')
        return AdmCustomer.objects.all()
    
    def resolve_all_accounts(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return AdmAccount.objects.select_related('admcustomer').all()


    def resolve_customer(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return AdmCustomer.objects.get(pk=id)

        if name is not None:
            return AdmCustomer.objects.get(name=name)
        
        return None
    

    def resolve_account(self, info , **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return AdmAccount.objects.get(pk=id)
        
        if name is not None:
            return AdmAccount.objects.get(name=name)
        
        return None




class CreateAdmCustomer(graphene.Mutation):
    
    logger.debug(f'CreateAdmCustomer funtion')

    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        zipcode = graphene.String(required=True)
        country = graphene.String(required=True)
        currency = graphene.String(required=True)
        status = graphene.String(required=True)
        customer_type = graphene.String(required=True)

    # The class attributes define the response of the mutation
    customer = graphene.Field(AdmCustomerType)

    @staticmethod
    def mutate(self, info, name, email, phone, city, state, zipcode, country, currency, status, customer_type):
        customer = AdmCustomer( name=name, email=email, phone=phone, city=city, state=state, zipcode=zipcode, country=country, currency=currency, status=state, customer_type=customer_type)

        customer.save()# Save data to SQL 
        
        # Notice we return an instanace of this mutation
        return CreateAdmCustomer(customer=customer)



# Create Input Object Types
class AdmCustomerInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zipcode = graphene.String()
    country = graphene.String()
    currency = graphene.String()
    status = graphene.String()
    customer_type = graphene.String()
    google_map_key = graphene.String()


class UpdateAdmCustomer(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = AdmCustomerInput(required=True)
    
    customer_instance = graphene.Field(AdmCustomerType)

    @staticmethod
    def mutate(self,info, id, input=None):

        #print("asfasfasfasfasf")

        customer_instance = AdmCustomer.objects.get(pk=id)

        if customer_instance :

            customer_instance.name = input.name
            customer_instance.google_map_key = input.google_map_key
            customer_instance.save() # Save data to SQL

            return UpdateAdmCustomer(customer_instance=customer_instance)

        return UpdateAdmCustomer(customer_instance=None)



class DeleteAdmCustomer(graphene.Mutation):

    # Return values
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info , id):
        customer = AdmCustomer.objects.get(id=id)
        print("DEBUG: %s:%s" % (customer.id, customer.name))
        customer.delete()

        return DeleteAdmCustomer(
            id=id,
            name=customer.name
        )



class Mutation(graphene.ObjectType):

    Create_AdmCustomer_link = CreateAdmCustomer.Field()
    Update_AdmCustomer_link = UpdateAdmCustomer.Field()
    Delete_AdmCustomer_link = DeleteAdmCustomer.Field()
    