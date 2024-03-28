from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render

from common.permissions.shop import ShopPermission

from shop.models import Shop
from shop.rest.serializers.shop import ShopSerializer

"""will add permissions classes for all views at the end"""

class ShopListCreateView(ListCreateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()

class ManageShopView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'
    # permission_classes = [ShopPermission]

