# from rest_framework import generics, authentication, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import *
from core.rest.serializers.user import (
    UserSerializer,
)

class ListCreateUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()



class ManageUserView(RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'
