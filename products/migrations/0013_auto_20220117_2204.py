# Generated by Django 3.2 on 2022-01-17 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20220117_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='like',
            new_name='favourites',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='is_fav',
        ),
    ]
