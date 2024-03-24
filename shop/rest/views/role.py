from rest_framework import generics
from django.shortcuts import render
from shop.models import Role
from shop.rest.serializers.role import RoleSerializer

class RoleListView(generics.ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()