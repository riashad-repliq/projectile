from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from shop.models import Shop
from product.models import Product, Image, ProductInventory
from product.rest.serializers.product import ProductSerializer, ManageProductSerializer, ListCreateProductSerializer
from common.permissions.shop import ShopPermission, ProductPermission

"""PUBLIC PRODUCT VIEWS"""

class ListProductView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        shop_slug= self.kwargs.get('shop_slug')

        shop = get_object_or_404(Shop, slug=shop_slug)

        products = Product.objects.filter(shop=shop)
        if not products:
            raise NotFound(detail="This shop does not have any products")

        return products

class RetrieveProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]



    def get_object(self):
        shop_slug = self.kwargs.get('shop_slug')
        shop = get_object_or_404(Shop, slug=shop_slug)
        product_slug = self.kwargs.get('product_slug')
        product = get_object_or_404(Product, slug=product_slug)
        return product

"""PRIVATE PRODUCT VIEWS"""

class ListCreateProductView(ListCreateAPIView):
    serializer_class = ListCreateProductSerializer
    permission_classes = [ProductPermission]

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        products = Product.objects.filter(shop=shop)
        return products

    def perform_create(self, serializer):
        shop_uuid= self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        product = serializer.save(shop=shop)
        return product

class ManageProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ManageProductSerializer
    queryset = Product.objects.filter()
    permission_classes = [ProductPermission]

    def get_object(self):
        """shop retrieval is done through the permission class"""

        product_uuid = self.kwargs.get('product_uuid')
        product = get_object_or_404(Product, uuid=product_uuid)
        return product

    def perform_update(self, serializer,*args, **kwargs):

        instance = serializer.save()

        if 'image' in self.request.data:
            data_set = self.request.data.getlist('image')
            print(data_set)
            for image in data_set:
                Image.objects.create(image=image, product=instance)

        if 'quantity' in self.request.data:
            product_inventory = get_object_or_404(ProductInventory, product=instance)
            product_inventory.quantity = self.request.data.get('quantity')['quantity']
            product_inventory.save()
