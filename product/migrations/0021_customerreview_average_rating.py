# Generated by Django 5.0.3 on 2024-04-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_remove_image_farce'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerreview',
            name='average_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]