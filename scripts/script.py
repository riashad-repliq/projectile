from core.models import *
from product.models import *
from django.http import request
from cart.models import *

# def run():
#     shop , created = Shop.objects.get_or_create(name= 'myShop', owner_id= User.objects.first().id)
#     # user = User.objects.first()
#     # member, created = member.objects.get_or_create(shop = shop , user = user , member_type = 'staff' )

#     print(shop.members.all())
import random
from faker import Faker
def run():
    faker = Faker()
    print(faker.uuid4())


