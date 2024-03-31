from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import serializers
from common.helper import DynamicFieldsModelSerializer
from cart.models import *

class ManageCartItemSerializer(DynamicFieldsModelSerializer):
    shop_product = serializers.UUIDField(source= 'shop_product.uuid', read_only=True)
    cart_item_total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['uuid', 'shop_product', 'quantity', 'cart_item_total_price']

    def get_cart_item_total_price(self, obj):
        return obj.calculate_price()




class ListCreateCartItemSerializer(DynamicFieldsModelSerializer):
    shop_product = serializers.UUIDField(source= 'shop_product.uuid')
    cart_item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['uuid', 'shop_product', 'quantity', 'cart_item_total_price']

    def get_cart_item_total_price(self, obj):
        return obj.calculate_price()

    def create(self, validated_data):
        shop_product_uuid = validated_data.get('shop_product')['uuid']
        shop_product = get_object_or_404(ShopProduct, uuid=shop_product_uuid)
        quantity = validated_data.get('quantity')
        cart = self.context['request'].user.cart
        cart_item = CartItem.objects.create(cart=cart, shop_product=shop_product, quantity=quantity)
        return cart_item
