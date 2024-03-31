# Generated by Django 5.0.3 on 2024-03-31 07:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_uuid_alter_shopproduct_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ab9c4ae9-f608-4579-a30d-119e24cbb2a5'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3913808c-0cfd-4bba-b9a1-6b62dac3328f'), editable=False, unique=True),
        ),
    ]