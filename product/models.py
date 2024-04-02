import uuid

from django.db import models
from django.utils.text import slugify
from versatileimagefield.fields import VersatileImageField
from autoslug import AutoSlugField

from shop.models import Shop

class Product(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    product_profile_image = VersatileImageField(blank=True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    name = models.CharField(max_length= 30, unique=True)

    def __str__(self):
        return self.name

class TaggedProduct(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="product_tags")
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.product.name} tagged with {self.tag.name}'