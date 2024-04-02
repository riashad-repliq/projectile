from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from order.models import Order, OrderItem

class OrderSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Order
        fields = ['uuid', 'total_amount', 'order_date', 'delivery_status', 'order_items']



class OrderItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']