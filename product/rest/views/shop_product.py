from common.permissions.shop import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.shortcuts import render
from shop.models import Shop
from product.models import Product, ShopProduct
from product.rest.serializers.shop_product import PrivateShopProductSerializer
from rest_framework.exceptions import NotFound


class ShopProductListCreateView(ListCreateAPIView):
    serializer_class = PrivateShopProductSerializer
    permission_classes = [ShopPermission]

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        # Getting product
        products = ShopProduct.objects.filter(shop=shop)
        if not products:
            raise NotFound(detail="This shop does not have any products")

        return products
    def perform_create(self, serializer):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        serializer.save(shop=shop)

class ManageShopProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateShopProductSerializer
    queryset = Product.objects.filter()
    permission_classes = [ShopPermission]

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        #  Getting product uuid
        shop_product_uuid = self.kwargs.get('shop_product_uuid', None)

        try:
            product = ShopProduct.objects.get(uuid=shop_product_uuid)
        except ShopProduct.DoesNotExist:
            raise NotFound(detail="This shop does not sell this product")

        return product

