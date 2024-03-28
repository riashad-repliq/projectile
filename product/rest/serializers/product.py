from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import *

# class ProductSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         read_only_fields= ['uuid']

class ShopProductSerializer(DynamicFieldsModelSerializer):
    product_info = serializers.SerializerMethodField()
    shop_info= serializers.SerializerMethodField()

    class Meta:
        model = ShopProduct
        fields = ['uuid',  'product_info', 'shop_info']
        read_only_fields = ['uuid']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid
        }

    def get_shop_info(self, obj):
        shop = obj.shop
        return {
            'uuid': shop.uuid,
            'shop_name': shop.name,
            'location': shop.location,

        }

