# Generated by Django 3.2 on 2022-01-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_calory_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_gluten',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
