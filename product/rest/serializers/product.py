from django.shortcuts import get_object_or_404
# from django.db.models import get_or_create

from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import Product

"""Public Product Serializers"""
class ProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid','slug', 'name', 'description', 'price','product_profile_image', 'quantity' ]



"""Private Product Serializers"""
class ListCreateProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'price','product_profile_image', 'quantity']


class ManageProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'price', 'quantity']
