# Generated by Django 5.0.3 on 2024-04-02 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('product', '0007_alter_product_uuid_alter_tag_uuid_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]