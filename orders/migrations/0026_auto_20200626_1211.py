# Generated by Django 2.1.5 on 2020-06-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_orders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='price',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
