# Generated by Django 5.0.3 on 2024-03-28 14:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('shop', 'user')},
        ),
    ]