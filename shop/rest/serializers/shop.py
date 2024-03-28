from common.helper import DynamicFieldsModelSerializer

from core.models import User
from shop.models import Shop, Member
from rest_framework import serializers
from shop.rest.serializers.member import MemberSerializer

class ShopSerializer(DynamicFieldsModelSerializer):
    members = MemberSerializer(many=True, read_only = True, fields=('uuid', 'user_uuid', 'username', ))

    class Meta:
        model = Shop
        fields = ['uuid', 'name', 'location', 'members']
        read_only_fields = ['uuid']


    # def create(self, validated_data):
    #     shop = Shop.objects.create(**validated_data)
    #     return shop

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.location = validated_data.get('location', instance.location)
    #     instance.save()
    #     return instance

