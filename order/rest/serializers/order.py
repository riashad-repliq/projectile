from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from order.models import Order, OrderItem

class OrderItemSerializer(DynamicFieldsModelSerializer):
    product = serializers.CharField(source='product.uuid')
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']
    def get_price(self, obj):
        return obj.calculate_price()


class OrderSerializer(DynamicFieldsModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['uuid', 'total_amount', 'order_date', 'delivery_status', 'order_items']


class CreateOrderSerializer(serializers.Serializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    delivery_status = serializers.CharField(max_length=100, read_only=True)


class OrderItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']