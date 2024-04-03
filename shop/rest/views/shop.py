from rest_framework.generics import   ListAPIView , RetrieveAPIView,  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.permissions.shop import *

from shop.models import Shop, Member
from shop.rest.serializers.shop import PublicShopSerializer, PrivateShopSerializer, ListShopSerializer

"""Public Views"""

class ShopListCreateView(ListCreateAPIView):
    serializer_class = PublicShopSerializer
    queryset = Shop.objects.filter()
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        shop= serializer.save()

        user = self.request.user
        Member.objects.create(shop =shop, user = user, member_type ='owner')

class RetrieveShopView(RetrieveAPIView):
    serializer_class = PublicShopSerializer
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        shop_slug = self.kwargs.get('shop_slug')
        shop = get_object_or_404(Shop, slug=shop_slug)
        return shop

"""Private Views"""

class ListShopView(ListAPIView):
    serializer_class = ListShopSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Shop.objects.filter(members__user=user)




class ManageShopView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateShopSerializer
    queryset = Shop.objects.filter()
    # authentication_classes = [JWTAuthentication]
    permission_classes= [ShopPermission]

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        return shop


