# Generated by Django 2.1.5 on 2020-06-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20200626_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='large',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pasta_salads',
            name='large',
            field=models.FloatField(null=True),
        ),
    ]
