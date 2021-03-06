# Generated by Django 3.2 on 2022-01-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=3, null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='title',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
