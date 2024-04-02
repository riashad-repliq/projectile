from django.contrib import admin
from product.models import Product, Tag, TaggedProduct
admin.site.register(Product)

admin.site.register(Tag)
admin.site.register(TaggedProduct)