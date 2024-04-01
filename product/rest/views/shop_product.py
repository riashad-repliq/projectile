from common.permissions.shop import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from django.shortcuts import render
from shop.models import Shop
from product.models import Product, ShopProduct
from product.rest.serializers.shop_product import *
from product.rest.serializers.product import NewProductSerializer
from rest_framework.exceptions import NotFound


"""PUBLIC VIEWS"""
class ListShopProductView(ListAPIView):
    serializer_class = PublicListShopProductSerializer


    def get_queryset(self):
        shop_slug = self.kwargs.get('shop_slug')
        shop = get_object_or_404(Shop, slug=shop_slug)

        shop_products = ShopProduct.objects.filter(shop=shop)
        if not shop_products:
            raise NotFound(detail="This shop does not have any products")

        return shop_products


class RetrieveShopProductView(RetrieveAPIView):
    serializer_class = PublicShopProductSerializer
    queryset = Product.objects.filter()

    def get_object(self):
        shop_slug = self.kwargs.get('shop_slug')

        try:
            shop = Shop.objects.get(slug=shop_slug)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        shop_product_slug = self.kwargs.get('shop_product_slug', None)

        try:
            product = ShopProduct.objects.get(slug=shop_product_slug)
        except ShopProduct.DoesNotExist:
            raise NotFound(detail="This shop does not sell this product")

        return product



"""PRIVATE VIEWS"""
class ShopProductListCreateView(ListCreateAPIView):
    serializer_class = PrivateListCreateShopProductSerializer
    permission_classes = [ShopPermission]

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        shop_products = ShopProduct.objects.filter(shop=shop)
        if not shop_products:
            raise NotFound(detail="This shop does not have any products")

        return shop_products

    def perform_create(self, serializer):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        serializer.save(shop=shop)

class ManageShopProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateManageShopProductSerializer
    queryset = Product.objects.filter()
    permission_classes = [ShopPermission]

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        shop_product_uuid = self.kwargs.get('shop_product_uuid', None)

        try:
            product = ShopProduct.objects.get(uuid=shop_product_uuid)
        except ShopProduct.DoesNotExist:
            raise NotFound(detail="This shop does not sell this product")

        return product


class CreateNewProduct(CreateAPIView):
    serializer_class = NewProductSerializer
    permission_classes = [ShopPermission]

    def perform_create(self, serializer):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = Shop.objects.get(uuid=shop_uuid)
        quantity = self.request.data.get('quantity')

        product =serializer.save(introduced_by=shop)
        ShopProduct.objects.create(product = product, quantity = quantity, shop = shop)