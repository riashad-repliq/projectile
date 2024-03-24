from rest_framework import generics
from django.shortcuts import render
from shop.models import Shop
from shop.rest.serializers.shop import ShopSerializer

class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

class ManageShopView(generics.RetrieveUpdateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

class DeleteShopView(generics.DestroyAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
