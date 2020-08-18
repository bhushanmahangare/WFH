import graphene
import logging

from graphene_django.types import DjangoObjectType
from network.models import Location
from authentication.models import AdmCustomer
from authentication.schema import AdmCustomerInput

logger = logging.getLogger(__name__)


class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class Query(object):

    location = graphene.Field(
        LocationType,
        id=graphene.Int(),
        name=graphene.String()
    )

    def resolve_location(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Location.object.get(pk=id)
        
        return None

    all_locations = graphene.List(LocationType)

    def resolve_all_locations(self, info , **kwargs):
        return Location.objects.all()


class LocationInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    hotspotenable = graphene.Boolean()
    autologinenable = graphene.Boolean()
    automacregister = graphene.Boolean()
    autologinvalidity = graphene.Int()
    autologinvalidity_unit = graphene.Int()
    interiminterval = graphene.Int()
    #customer = graphene.ID()
    customer = graphene.Field(AdmCustomerInput)


class CreateLocationMutation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        location_data = LocationInput(required=True)

    def mutate(self, info, location_data=None):

        #customer = AdmCustomer.objects.get(pk = location_data.customer)

        location = Location(
            name = location_data.name,
            hotspotenable = location_data.hotspotenable,
            autologinenable = location_data.autologinenable,
            automacregister = location_data.automacregister,
            autologinvalidity = location_data.autologinvalidity,
            autologinvalidity_unit = location_data.autologinvalidity_unit,
            interiminterval = location_data.interiminterval,
            customer = location_data.customer,
        )
        location.save()

        return CreateLocationMutation(location=location)


class Mutation(graphene.ObjectType):

    Create_Location_link = CreateLocationMutation.Field() 