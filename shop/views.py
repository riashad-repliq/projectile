from rest_framework import generics
from django.shortcuts import render
from .models import *
from shop.rest.serializers.shop import *

class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

class ManageShopView(generics.RetrieveUpdateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()



class RoleListView(generics.ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()