import graphene
import logging

from graphene_django.types import DjangoObjectType
from smartap.models import AP

logger = logging.getLogger(__name__)

class APType(DjangoObjectType):
    class Meta:
        model = AP


class Query(object):

    ap = graphene.Field(
        APType,
        id = graphene.Int(),
        macaddress = graphene.String()
    )

    def resolve_ap(self, info, **kwargs):
        id = kwargs.get('id')
        macaddress = kwargs.get('macaddress')

        if id is not None:
            return AP.object.get(pk=id)

    all_aps = graphene.List(APType)

    def resolve_all_aps(self, info, **kwargs):
        return AP.objects.all()