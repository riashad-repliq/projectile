import uuid

from django.db import models
from core.models import User

class Shop (models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Member(models.Model):

    members = (
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),

    )
    uuid = models.UUIDField( default=uuid.uuid4, unique=True, editable=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name = 'members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=50, choices = members)
    # is_default= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member_type} at {self.shop}'