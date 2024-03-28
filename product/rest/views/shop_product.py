from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.shortcuts import render
from shop.models import Shop
from product.models import Product, ShopProduct
from product.rest.serializers.product import ShopProductSerializer
from rest_framework.exceptions import NotFound

"""will add permissions classes for all views at the end"""

class ShopProductListCreateView(ListCreateAPIView):
    serializer_class = ShopProductSerializer

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        # Getting product
        products = Product.objects.filter(shopproduct__shop=shop)
        if not products:
            raise NotFound(detail="This shop does not have any products")

        return products

class ManageShopProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShopProductSerializer
    queryset = Product.objects.filter()

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        #  Getting product uuid
        product_uuid = self.kwargs.get('product_uuid', None)

        try:
            product = ShopProduct.objects.get(product__uuid=product_uuid)
        except ShopProduct.DoesNotExist:
            raise NotFound(detail="Product does not exist")


        return product

