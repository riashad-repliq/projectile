# Generated by Django 5.0.3 on 2024-03-31 06:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_uuid_alter_shopproduct_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e8468c87-61ed-4634-bc6e-4ab404724cff'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('db8ae4b7-1c92-48ec-a4bd-8272ad5faf76'), editable=False, unique=True),
        ),
    ]