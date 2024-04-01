from django.contrib.auth import get_user_model
from common.helper import DynamicFieldsModelSerializer

from shop.models import Shop, Member
from rest_framework import serializers
from shop.rest.serializers.member import ManageMemberSerializer
from product.rest.serializers.shop_product import *

User=get_user_model()


"""Public Serializers"""

class PublicShopSerializer(DynamicFieldsModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['uuid','slug','name', 'location', 'products']
        read_only_fields = ['uuid']

    def get_products(self, obj):
        shop_products = obj.shop_products.all()
        serializer = PublicShopProductSerializer(shop_products, many=True, read_only=True, fields=('uuid', 'quantity','product_info'))
        return serializer.data


"""Private Serializers"""

class PrivateShopSerializer(DynamicFieldsModelSerializer):
    members = ManageMemberSerializer(many=True, read_only=True, fields=('uuid', 'user_uuid', 'username'))
    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['uuid', 'name', 'location', 'members', 'products']
        read_only_fields = ['uuid', 'members', 'products']

    def get_products(self, obj):
        shop_products = obj.shop_products.filter()
        serializer = PrivateManageShopProductSerializer(shop_products, many=True, fields=('uuid', 'product_info'))
        return serializer.data