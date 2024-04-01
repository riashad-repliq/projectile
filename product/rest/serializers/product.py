from django.shortcuts import get_object_or_404
# from django.db.models import get_or_create

from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import *

from product.rest.serializers.tags import TagSerializer, TaggedShopProductSerializer

class NewProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'product_profile_image', 'quantity']

    def create(self, validated_data):
        quantity = validated_data.pop('quantity')
        product = Product.objects.create(**validated_data)

        return product
