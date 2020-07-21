from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]


#urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
#]