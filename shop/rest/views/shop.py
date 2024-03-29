from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from django.shortcuts import render

from common.permissions.shop import *

from shop.models import Shop, Member
from shop.rest.serializers.shop import PublicShopSerializer, PrivateShopSerializer

"""Public Views"""

class ShopListCreateView(ListCreateAPIView):
    serializer_class = PublicShopSerializer
    queryset = Shop.objects.filter()

    def perform_create(self, serializer):
        shop= serializer.save()

        user = self.request.user
        member = Member.objects.create(shop =shop, user = user, member_type ='owner')

class RetrieveShopView(RetrieveAPIView):
    serializer_class = PublicShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'

"""Private Views"""

class ManageShopView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateShopSerializer
    queryset = Shop.objects.filter()
    lookup_field = 'uuid'



