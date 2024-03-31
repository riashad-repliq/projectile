import uuid
from django.db import models

from core.models import User
from product.models import ShopProduct

class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"{self.user.username}'s cart"

    def calculate_total_cart_price(self):
        total_price = 0
        for cart_item in self.cart_items.filter():
            total_price += cart_item.calculate_price()
        return total_price



class CartItem (models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    shop_product =models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.shop_product.product.name} from {self.shop_product.shop.name}"

    def calculate_price(self):
        return self.shop_product.product.price * self.quantity


