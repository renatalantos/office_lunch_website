# Generated by Django 3.2 on 2022-01-11 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20220105_1429'),
        ('till', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComponentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grilled', models.CharField(blank=True, max_length=11, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('componentitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentitems', to='till.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]
