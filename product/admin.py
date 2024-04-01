from django.contrib import admin
from product.models import Product, ShopProduct, Tag, TaggedShopProduct
admin.site.register(Product)
admin.site.register(ShopProduct)
admin.site.register(Tag)
admin.site.register(TaggedShopProduct)