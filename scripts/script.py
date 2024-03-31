from core.models import *
from product.models import *

# def run():
#     shop , created = Shop.objects.get_or_create(name= 'myShop', owner_id= User.objects.first().id)
#     # user = User.objects.first()
#     # member, created = member.objects.get_or_create(shop = shop , user = user , member_type = 'staff' )

#     print(shop.members.all())

def run():
    shop_product = ShopProduct.objects.get(uuid="54fad857-a7bf-448e-8e2f-42af00d785f0")
    print (shop_product)