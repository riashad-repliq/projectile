from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from order.models import Order

class OrderSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Order
        fields = ['uuid', 'customer', 'total_amount', 'order_date', 'delivery_status', 'order_items']


class DirectOrderSerializer(serializers.Serializer):
    shop_product_uuid = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1)