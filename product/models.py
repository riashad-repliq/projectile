import uuid

from django.db import models

from versatileimagefield.fields import VersatileImageField
from autoslug import AutoSlugField

from shop.models import Shop

class Product(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    product_profile_image = VersatileImageField(blank=True, null= True, upload_to= 'images/product_profile')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.ManyToManyField('Inventory', through='ProductInventory', related_name='product_inventory')

    def __str__(self):
        return self.name

class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = VersatileImageField(blank=True, null= True, upload_to='images/')

    def __str__(self):
        return f"image of {self.product.name}"


class Inventory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inventory of {self.shop.name}"


class ProductInventory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    inventory= models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_items')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} left of {self.product.name}'


class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)


class ProductTag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')

    class Meta:
        unique_together = ('tag', 'product')