from core.models import User
from shop.models import Shop, Role
from rest_framework import serializers
from shop.rest.serializers.role import RoleSerializer

class ShopSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only = True)

    class Meta:
        model = Shop
        fields = ['uuid', 'name', 'location', 'roles']
        read_only_fields = ['uuid']



    # def create(self, validated_data):
    #     shop = Shop.objects.create(**validated_data)
    #     return shop

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.location = validated_data.get('location', instance.location)
    #     instance.save()
    #     return instance

