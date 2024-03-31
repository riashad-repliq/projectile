from rest_framework import serializers
from common.helper import DynamicFieldsModelSerializer

from cart.models import Cart
from cart.rest.serializers.cart_item import ManageCartItemSerializer

class CartSerializer(DynamicFieldsModelSerializer):
    cart_items = ManageCartItemSerializer(many=True, read_only=True, fields =('uuid','shop_product', 'quantity', 'cart_item_total_price' ))
    cart_total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['cart_total_price' ,'cart_items']
        read_only_fields = ['uuid']

    def get_cart_total_price(self,obj):
        return obj.calculate_total_cart_price()