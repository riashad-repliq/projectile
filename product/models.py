import uuid

from django.db import models

from versatileimagefield.fields import VersatileImageField

from shop.models import Shop

class Product(models.Model):

    uuid = models.UUIDField( default=uuid.uuid4(), unique=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    product_profile_image = VersatileImageField(blank=True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_by = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShopProduct(models.Model):

    uuid = models.UUIDField( default=uuid.uuid4(), unique=True, editable=False)
    shop = models.ForeignKey(Shop, on_delete= models.CASCADE )
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()
