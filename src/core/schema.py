import graphene
import authentication.schema
import authentication.schema_relay
import network.schema
import smartap.schema
import graphql_jwt


class Query( 
    authentication.schema.Query,  
    authentication.schema_relay.Query, 
    network.schema.Query, 
    smartap.schema.Query,
    graphene.ObjectType     ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation( 
    authentication.schema.Mutation, 
    network.schema.Mutation,
    smartap.schema.Mutation,  
    graphene.ObjectType     ):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    

schema = graphene.Schema( query = Query  , mutation = Mutation)