import uuid

from django.db import models
from django.utils.text import slugify
from versatileimagefield.fields import VersatileImageField
from autoslug import AutoSlugField

from shop.models import Shop

class Product(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    product_profile_image = VersatileImageField(blank=True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    introduced_by = models.ForeignKey(Shop, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.name


class ShopProduct(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    # slug = AutoSlugField(populate_from=)
    shop = models.ForeignKey(Shop, on_delete= models.CASCADE, related_name='shop_products' )
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('shop', 'product')

    def save(self, *args, **kwargs):
        if not self.slug:
            concatenated_names = f"{self.shop.name}-{self.product.name}"
            self.slug = slugify(concatenated_names)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.product} in {self.shop.name}'



class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    name = models.CharField(max_length= 30, unique=True)

    def __str__(self):
        return self.name

class TaggedShopProduct(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    shop_product = models.ForeignKey(ShopProduct, on_delete= models.CASCADE, related_name="shop_product_tags")
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.shop_product.product.name} tagged with {self.tag.name}'