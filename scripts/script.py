from core.models import *

# def run():
#     shop , created = Shop.objects.get_or_create(name= 'myShop', owner_id= User.objects.first().id)
#     # user = User.objects.first()
#     # member, created = member.objects.get_or_create(shop = shop , user = user , member_type = 'staff' )

#     print(shop.members.all())

def run():
    user, created = User.objects.get_or_create(phone_number= 12345555, password='randalthor2001')
    user.username = 'MYname'
    print(user.phone_number,user.username)