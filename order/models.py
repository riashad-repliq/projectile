import uuid
from django.db import models

from django.contrib.auth import get_user_model
from product.models import ShopProduct

User= get_user_model()
class Order(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES)

    def __str__(self):
        return f"Order no {self.order_unique_id}"

class OrderItem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    order = models.ForeignKey(Order, on_delete= models.CASCADE, related_name='order_items')
    shop_product = models.ForeignKey(ShopProduct, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.shop_product.product.name} from {self.shop_product.shop.name}"
