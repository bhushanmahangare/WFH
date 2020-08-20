import graphene
import logging

from graphene_django.types import DjangoObjectType
from network.models import Location
from authentication.models import AdmCustomer
from .forms import CreateLocationForm

logger = logging.getLogger(__name__)


class LocationFields():
    id = graphene.ID()
    name = graphene.String()
    hotspotenable = graphene.Boolean()
    autologinenable = graphene.Boolean()
    automacregister = graphene.Boolean()
    autologinvalidity = graphene.Int()
    autologinvalidity_unit = graphene.Int()
    interiminterval = graphene.Int()
    customer = graphene.Int()

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class LocationErrorsInputType(graphene.ObjectType, LocationFields):
     id = graphene.String()
     customer = graphene.String()

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
    customerid = graphene.Int()

class CreateLocationMutation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        location_data = LocationInput(required=True)

    ok = graphene.Boolean()
    location = graphene.Field(LocationType)
    errors = graphene.Field(LocationErrorsInputType)

    @staticmethod
    def mutate(self, info, location_data):
        form = CreateLocationForm(data=location_data)
        
        if form.is_valid():
            location = form.save()
            return CreateLocationMutation(ok=True, location=location, errors=form.errors)
        return CreateLocationMutation(ok=False, errors=form.errors)

        '''customerid = AdmCustomer.objects.get(id=location_data.customerid)

        location = Location(
            name = location_data.name,
            hotspotenable = location_data.hotspotenable,
            autologinenable = location_data.autologinenable,
            automacregister = location_data.automacregister,
            autologinvalidity = location_data.autologinvalidity,
            autologinvalidity_unit = location_data.autologinvalidity_unit,
            interiminterval = location_data.interiminterval,
            customer = customerid
        )
        location.save()

        return CreateLocationMutation(location=location)'''


class UpdateLocationMutation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        location_data = LocationInput(required=True)

    @staticmethod
    def get_object(id):
        return Location.objects.get(pk=id)

    def mutate(self, info, location_data=None):

        location = UpdateLocationMutation.get_object(location_data.id)
        customerid = AdmCustomer.objects.get(id=location_data.customerid)

        if Location.objects.filter(name=location_data.name).exists():
            #return ('user or token or other data that you need in'
                #'mutation, this is not mutation return value')
            return UpdateLocationMutation(location='Error')

        else:
            if location_data.name:
                location.name = location_data.name
            if location_data.hotspotenable:
                location.hotspotenable = location_data.hotspotenable
            if location_data.autologinenable:
                location.autologinenable = location_data.autologinenable
            if location_data.automacregister:
                location.automacregister = location_data.automacregister
            if location_data.autologinvalidity:
                location.autologinvalidity = location_data.autologinvalidity
            if location_data.autologinvalidity_unit:
                location.autologinvalidity_unit = location_data.autologinvalidity_unit
            if location_data.interiminterval:
                location.interiminterval = location_data.interiminterval

            location.save()

            return UpdateLocationMutation(location=location)


class Mutation(graphene.ObjectType):

    Create_Location_link = CreateLocationMutation.Field() 
    Update_Location_link = UpdateLocationMutation.Field()