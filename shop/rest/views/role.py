from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import render
from shop.models import Role
from shop.rest.serializers.role import RoleSerializer

"""will add permissions classes for all views at the end"""


class RoleListView(ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()

class CreateRoleView(CreateAPIView):
    serializer_class = RoleSerializer

class DetailRoleView(RetrieveAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()
    lookup_field = 'uuid'

class UpdateRoleView(UpdateAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()
    lookup_field = 'uuid'

class DeleteRoleView(DestroyAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()
    lookup_field = 'uuid'