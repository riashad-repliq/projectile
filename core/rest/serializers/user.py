from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers
from shop.models import Role

from core.rest.serializers.role import UserRoleSerializer

class UserSerializer(serializers.ModelSerializer):
    roles = UserRoleSerializer(many=True,  source = 'role_set')

    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'password', 'username', 'roles']
        extra_kwargs ={'password': {'write_only': True, 'min_length':5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user