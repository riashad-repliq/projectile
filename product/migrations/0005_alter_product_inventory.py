# Generated by Django 5.0.3 on 2024-04-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productinventory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.ManyToManyField(related_name='product_inventory', through='product.ProductInventory', to='product.inventory'),
        ),
    ]
