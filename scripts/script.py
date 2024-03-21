from core.models import *

def run():
    shop , created = Shop.objects.get_or_create(name= 'myShop', owner_id= User.objects.first().id)
    # user = User.objects.first()
    # role, created = Role.objects.get_or_create(shop = shop , user = user , role_type = 'staff' )

    print(shop.roles.all())