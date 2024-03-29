from django.shortcuts import get_object_or_404
from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import *

class PrivateShopProductSerializer(DynamicFieldsModelSerializer):
    product_info = serializers.SerializerMethodField()

    class Meta:
        model = ShopProduct
        fields = ['uuid', 'product_info', 'quantity']

        read_only_fields = ['uuid']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid
        }
    def create(self, validated_data):
        product_uuid = validated_data.pop('product_uuid')
        shop_product = get_object_or_404(Product, uuid=product_uuid)


        product = ShopProduct.objects.create(product= shop_product,**validated_data)
        return product

class PublicShopProductSerializer(DynamicFieldsModelSerializer):
    product_info = serializers.SerializerMethodField()

    class Meta:
        model = ShopProduct
        fields = ['uuid',  'product_info']
        read_only_fields = ['uuid']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid
        }
