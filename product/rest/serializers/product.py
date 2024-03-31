from django.shortcuts import get_object_or_404
from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import *


class NewProductSerializer(DynamicFieldsModelSerializer):
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'product_profile_image', 'quantity']

    def create(self, validated_data):
        # shop_uuid = self.context['view'].kwargs['shop_uuid']
        # shop = Shop.objects.get(uuid=shop_uuid)
        # quantity = validated_data.pop('quantity', None)

        product = Product.objects.create(**validated_data)
        # shop_product = ShopProduct.objects.create(product=product, shop=shop, quantity=quantity)

        return product
