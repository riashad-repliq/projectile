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

    def get_object(self):
        shop_slug = self.kwargs.get('shop_slug')
        shop = get_object_or_404(Shop, slug=shop_slug)
        return shop

"""Private Views"""

class ManageShopView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateShopSerializer
    permission_classes= [ShopPermission]

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        return shop


