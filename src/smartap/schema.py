import graphene
import logging

# GENERAL DJANGO IMPORTS
from django.core.exceptions import ValidationError


# GRAPHENE IMPORTS
from graphene import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


# PROJECT IMPORTS
from smartap.models import AP
from helper.controlcenterutils import ControlCenterUtils


logger = logging.getLogger(__name__)


def getErrors(e):
    # transform django errors to redux errors
    # django: {"key1": [value1], {"key2": [value2]}}
    # redux: ["key1", "value1", "key2", "value2"]
    fields = e.message_dict.keys()
    messages = ['; '.join(m) for m in e.message_dict.values()]
    errors = [i for pair in zip(fields, messages) for i in pair]
    return errors


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


'''class APNode(DjangoObjectType):
    class Meta:
        model = AP
        interfaces = (Node,)
        filter_fileds = {
            "macaddress" : [ "exact" , "icontanins" , "istartswith", ],
            "createdon" : ["exact"],
        }
class Query(object):
    ap = Node.Field(APNode)
    all_aps = DjangoFilterConnectionField(APNode)'''



class CreateAP(graphene.Mutation):
    
    logger.debug(f'CreateAdmCustomer funtion')

    class Arguments:
        # The input arguments for this mutation
        macaddress = graphene.String(required=True)
        wifilanserverid = graphene.Int(required=True)
        wifilancustomerid = graphene.Int(required=True)
        wifilanlocationid = graphene.Int(required=True)
        wifilanapid = graphene.Int(required=True)
        

    # The class attributes define the response of the mutation
    ap = graphene.Field(APType)

    @staticmethod
    def mutate(self, info, macaddress, wifilanserverid ,wifilancustomerid, wifilanlocationid, wifilanapid):
        try:
            #controlcenterutils = ControlCenterUtils();
            controlCenterStatus = ControlCenterUtils.addAccessPointInControlCenter(self,macaddress)
            print("respone :: ", controlCenterStatus);

            if controlCenterStatus == True :
                ap = AP( macaddress=macaddress ,wifilanserverid=wifilanserverid , wifilancustomerid=wifilancustomerid , wifilanlocationid=wifilanlocationid, wifilanapid=wifilanapid)
                
                # Save data to Database
                ap.save() 

                return CreateAP(ap=ap)
                
            else:
                print("Error");

            
            # Notice we return an instanace of this mutation

                return CreateAP(ap=controlCenterStatus)

        except ValidationError as e : 
            return CreateAP(ap=None, errors=getErrors(e))

        
class Mutation(graphene.ObjectType):

    Create_AP_link = CreateAP.Field() 