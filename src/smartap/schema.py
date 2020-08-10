import graphene
import logging

# GENERAL DJANGO IMPORTS
from django.core.exceptions import ValidationError

# GRAPHENE IMPORTS
from graphene_django.types import DjangoObjectType

# PROJECT IMPORTS
from smartap.models import AP


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

            '''response = get_vehicle_info(reg_no)

            if response:
                cache_data = VehicleCache(registration_number=reg_no, 
                                        details=response)
                cache_data.save()
                parsed_response = self.parse_vehicle_data(reg_no, response)
                AGENT = Agent.objects.get(username='shailesh')
                vehicle_instance = Vehicle.objects.create(agent=AGENT, **parsed_response.get('vehicleInfo'))
                customer_instance = Customer.objects.create(vehicle_id=vehicle_instance.id, **parsed_response.get('customerInfo'))
                policy_instance = Policy.objects.create(vehicle_id=vehicle_instance.id, **parsed_response.get('policyInfo'))
                parsed_response.get('vehicleInfo').update({'id': vehicle_instance.id})
                parsed_response.get('customerInfo').update({'id': customer_instance.id})
                parsed_response.get('policyInfo').update({'id': policy_instance.id})                
                return parsed_response'''


            ap = AP( macaddress=macaddress ,wifilanserverid=wifilanserverid , wifilancustomerid=wifilancustomerid , wifilanlocationid=wifilanlocationid, wifilanapid=wifilanapid)

            # Save data to Database
            ap.save() 
            
            # Notice we return an instanace of this mutation
            return CreateAP(ap=ap)

        except ValidationError as e : 
            return CreateAP(ap=None, errors=getErrors(e))

        
class Mutation(graphene.ObjectType):

    Create_AP_link = CreateAP.Field()