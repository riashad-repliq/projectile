import uuid
from django.db import models
from django.contrib.auth import get_user_model

from versatileimagefield.fields import VersatileImageField
User = get_user_model()

from product.models import Product
class Image(models.Model):
    uuid = models.UUIDField(default= uuid.uuid4, editable=False, unique=True)
    image = VersatileImageField()
    added_by = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return self.uuid

class ProductImage(models.Model):
    uuid = models.UUIDField(default= uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'image of {self.product.name}'