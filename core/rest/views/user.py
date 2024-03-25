from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import *
from core.rest.serializers.user import (
    UserSerializer,
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

class DestroyUserView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
