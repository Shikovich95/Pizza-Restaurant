# Generated by Django 2.1.5 on 2020-06-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_subs'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.CharField(max_length=64)),
                ('large', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='pasta_salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
