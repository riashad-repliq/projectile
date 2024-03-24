from django.db import models
from core.models import User

class Shop (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):

    roles = (
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),

    )
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name = 'roles')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_type = models.CharField(max_length=50, choices = roles)

    def __str__(self):

        return f'{self.role_type} at {self.shop}'