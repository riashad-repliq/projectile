from core.models import *
from product.models import *
from django.http import request
from cart.models import *
from order.models import *
from faker import Faker

faker = Faker()


def run():
    user =User.objects.create_user(phone_number="+8801827703879", password="riashad",username=faker.name(), )