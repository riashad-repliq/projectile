# Generated by Django 5.0.3 on 2024-04-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_customerreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
