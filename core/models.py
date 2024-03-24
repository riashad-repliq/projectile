""" CUSTOM USER MODEL AND A CUSTOM USER_MODEL_MANAGER """

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Manager for our custom user model"""

    def create_user(self, phone_number, password=None, **extra_fields):

        if not phone_number:
            raise ValueError("USER MUST HAVE A PHONE NUMBER")

        user = self.model(phone_number=phone_number, **extra_fields )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone_number, password):

        user = self.create_user(phone_number, password)
        user.is_staff =True
        user.is_superuser= True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    phone_number=models.CharField( max_length=50, unique=True)
    username = models.CharField(max_length=255)
    profile_image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects= UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number

