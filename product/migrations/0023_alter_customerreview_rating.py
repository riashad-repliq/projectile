# Generated by Django 5.0.3 on 2024-04-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_customerreview_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.IntegerField(choices=[('one', 'One'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
