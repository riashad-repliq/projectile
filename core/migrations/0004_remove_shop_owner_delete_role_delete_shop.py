# Generated by Django 5.0.3 on 2024-03-24 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_first_name_user_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]