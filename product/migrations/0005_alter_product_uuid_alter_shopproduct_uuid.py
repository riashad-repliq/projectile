# Generated by Django 5.0.3 on 2024-03-31 04:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_uuid_alter_shopproduct_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d9f1495e-2fda-4f9c-ad8f-c7b12584ecdb'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b52baa62-205c-40ab-9eb5-3fb7cc16c84c'), editable=False, unique=True),
        ),
    ]