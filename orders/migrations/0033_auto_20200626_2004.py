# Generated by Django 2.1.5 on 2020-06-26 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_auto_20200626_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pasta_salads',
            old_name='n',
            new_name='name',
        ),
    ]
