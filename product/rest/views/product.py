from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from product.models import Product
from product.rest.serializers.product import ProductSerializer

"""will add permissions classes for all views at the end"""

class ProductListCreateView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

class ManageProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    lookup_field = 'uuid'