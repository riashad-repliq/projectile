from django.contrib import admin
from product.models import Product, Image ,Tag, TaggedProduct
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(TaggedProduct)