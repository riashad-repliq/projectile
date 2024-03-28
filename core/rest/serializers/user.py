from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer
from shop.models import Member

from shop.rest.serializers.member import MemberSerializer

class UserSerializer(DynamicFieldsModelSerializer):
    members = MemberSerializer(many=True, fields=('member_uuid', 'shop_uuid', 'member_type'), source='member_set' , read_only = True,)

    class Meta:
        model = get_user_model()
        fields = ['uuid','phone_number', 'password', 'username', 'members']
        extra_kwargs ={
            'password': {'write_only': True, 'min_length':5},
            'uuid': {'read_only': True},
            }


    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user