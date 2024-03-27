# from rest_framework import generics, authentication, permissions
from rest_framework.generics import ListAPIView ,CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import *
from core.rest.serializers.user import (
    UserSerializer,
)

class ListUserView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

class CreateUserView(CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class RetrieveUserView(RetrieveAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'

    # def get_object(self):
    #     """Retrieve and return the authenticated user."""
    #     return self.request.user

class UpdateUserView(UpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'

class DestroyUserView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'

