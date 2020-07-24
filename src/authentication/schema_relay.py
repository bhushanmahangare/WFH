import graphene
import logging

from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from authentication.models import AdmCustomer, AdmAccount

logger = logging.getLogger(__name__)

# The data is exposed in Nodes, so you must create one for the links.
class AdmCustomerNode(DjangoObjectType):
    logger.debug(f'Policy updater for policy id {DjangoObjectType}')

    class Meta:
        model = AdmCustomer
        filter_fields = ['name', 'email', 'status']
        # Each node implements an interface with an unique ID (you’ll see the result of this in a bit).
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    # Uses the LinkNode with the relay_link field inside your new query.
    relay_customer = relay.Node.Field(AdmCustomerNode)


    # Defines the relay_links field as a Connection, which implements the pagination structure.
    list_admcustomers = DjangoFilterConnectionField(AdmCustomerNode)