from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from shop.models import Shop, Role
from shop.rest.serializers.role import RoleSerializer

"""will add permissions classes for all views at the end"""


class ShopRoleListCreateView(ListCreateAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        shop_uuid= self.kwargs.get('shop_uuid')
        print (shop_uuid)
        return Role.objects.filter(shop__uuid=shop_uuid)

class ManageShopRoleView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()
    lookup_field = 'uuid'