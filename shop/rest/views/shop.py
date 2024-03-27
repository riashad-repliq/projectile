from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import render
from shop.models import Shop
from shop.rest.serializers.shop import ShopSerializer

"""will add permissions classes for all views at the end"""

class ShopListView(ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()

class CreateShopView(CreateAPIView):
    serializer_class = ShopSerializer

class DetailShopView(RetrieveAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'

class UpdateShopView(UpdateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'

class DeleteShopView(DestroyAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'
