# Generated by Django 3.2 on 2022-01-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='default_email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
