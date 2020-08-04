import graphene
import logging

from graphene_django.types import DjangoObjectType
from network.models import Location

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

    all_locations = graphene.List(LocationType)

    def resolve_location(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Location.object.get(pk=id)
        
        return None

    def resolve_all_locations(self, info , **kwargs):
        return Location.objects.all()