from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from shop.models import Shop
from product.models import Product
from product.rest.serializers.product import ProductSerializer, ManageProductSerializer, ListCreateProductSerializer
from common.permissions.shop import ShopPermission

"""PUBLIC PRODUCT VIEWS"""

class ListProductView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        shop_slug= self.kwargs.get('shop_slug')
        try:
            shop = get_object_or_404(Shop, slug=shop_slug)
        except:
            raise NotFound(detail="No such shop exists.")

        products = Product.objects.filter(shop=shop)
        if not products:
            raise NotFound(detail="This shop does not have any products")

        return products

class RetrieveProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]



    def get_object(self):
        shop_slug = self.kwargs.get('shop_slug')
        try:
            shop = get_object_or_404(Shop, slug=shop_slug)
        except:
            raise NotFound(detail="No such shop exists.")

        product_slug = self.kwargs.get('product_slug')
        try:
            product = get_object_or_404(Product, slug=product_slug)
        except:
            raise NotFound(detail="No such product exists.")

        return product

"""PRIVATE PRODUCT VIEWS"""

class ListCreateProductView(ListCreateAPIView):
    serializer_class = ListCreateProductSerializer
    permission_classes = [ShopPermission]

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        products = Product.objects.filter(shop=shop)
        if not products:
            raise NotFound(detail="This shop does not have any products")

        return products

    def perform_create(self, serializer):
        shop_uuid= self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        product = serializer.save(shop=shop)
        return product

class ManageProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ManageProductSerializer
    queryset = Product.objects.filter()
    # authentication_classes = [JWTAuthentication]
    permission_classes = [ShopPermission]

    def get_object(self):
        product_uuid = self.kwargs.get('product_uuid')
        product = get_object_or_404(Product, uuid=product_uuid)
        if not product:
            raise NotFound(detail="product does not exist")

        return product