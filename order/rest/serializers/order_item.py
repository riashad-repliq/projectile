from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from order.models import OrderItem

class OrderItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['shop_product', 'quantity', 'price']