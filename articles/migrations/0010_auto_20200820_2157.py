# Generated by Django 3.1 on 2020-08-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200820_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='GFG is best', unique=True, verbose_name='URL Slug'),
        ),
    ]
