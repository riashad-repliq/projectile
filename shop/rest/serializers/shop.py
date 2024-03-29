from common.helper import DynamicFieldsModelSerializer

from core.models import User
from shop.models import Shop, Member
from rest_framework import serializers
from shop.rest.serializers.member import MemberSerializer
from product.rest.serializers.shop_product import *

"""Private Serializers"""

class PrivateShopSerializer(DynamicFieldsModelSerializer):
    members = MemberSerializer(many=True, read_only=True, fields=('uuid', 'user_uuid', 'username'))
    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['uuid', 'name', 'location', 'members', 'products']
        read_only_fields = ['uuid', 'members', 'products']

    def get_products(self, obj):
        shop_products = obj.shop_products.all()
        serializer = PrivateShopProductSerializer(shop_products, many=True, fields=('uuid', 'product_info'))
        return serializer.data

"""Public Serializers"""

class PublicShopSerializer(DynamicFieldsModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['uuid','name', 'location', 'products']
        read_only_fields = ['uuid']

    def get_products(self, obj):
        shop_products = obj.shop_products.all()
        serializer = PrivateShopProductSerializer(shop_products, many=True, read_only=True, fields=('uuid', 'product_info'))
        return serializer.data

