from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.http import Http404
from common.helper import DynamicFieldsModelSerializer

from product.models import *
from product.rest.serializers.tags import *



"""PUBLIC SERIALIZERS"""
class PublicShopProductSerializer(DynamicFieldsModelSerializer):
    product_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShopProduct
        fields = [ 'product_info', 'quantity']
        read_only_fields = ['uuid' ,'quantity']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid,
        }

class PublicListShopProductSerializer(DynamicFieldsModelSerializer):
    product_info = serializers.SerializerMethodField()
    tags = TaggedShopProductSerializer(many=True, source= 'shop_product_tags')

    class Meta:
        model = ShopProduct
        fields = [ 'product_info', 'quantity', 'tags']

        read_only_fields = ['uuid']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid
        }


"""PRIVATE SERIALIZERS"""
class PrivateListCreateShopProductSerializer(DynamicFieldsModelSerializer):
    product_uuid = serializers.UUIDField(write_only=True)
    product_info = serializers.SerializerMethodField()
    tags = TaggedShopProductSerializer(many=True, source= 'shop_product_tags')

    class Meta:
        model = ShopProduct
        fields = ['uuid', 'product_uuid', 'product_info', 'quantity', 'tags']

        read_only_fields = ['uuid']

    def get_product_info(self, obj):
        product = obj.product
        return {
            'product_name': product.name,
            'description': product.description,
            'uuid': product.uuid
        }
    def create(self, validated_data):
        shop_uuid = self.context['view'].kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        product_uuid = validated_data.pop('product_uuid')
        product = get_object_or_404(Product, uuid=product_uuid)

        if ShopProduct.objects.filter(shop=shop, product=product).exists():
            raise Http404('This shop already has this product')


        shop_product = ShopProduct.objects.create(product= product,**validated_data)
        return shop_product


class PrivateManageShopProductSerializer(DynamicFieldsModelSerializer):
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
            'uuid': product.uuid,

        }

