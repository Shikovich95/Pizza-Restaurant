# Generated by Django 2.1.5 on 2020-06-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20200626_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='user',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='comment',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
