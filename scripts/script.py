from core.models import *
from product.models import *
from django.http import request
from cart.models import *
from faker import Faker
faker =Faker()

def run():
    shop = Shop.objects.create(name='test-shop', location ='test-location')
    print (shop)


