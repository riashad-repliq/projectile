from shop.models import Shop, Role
from rest_framework import serializers
from shop.rest.serializers.role import RoleSerializer

class ShopSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'location', 'roles']

