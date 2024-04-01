from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.settings import api_settings


from core.models import *

from rest_framework_simplejwt.authentication import JWTAuthentication


from core.rest.serializers.user import (
    UserSerializer,
)

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(User, uuid=self.request.user.uuid)