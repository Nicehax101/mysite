# Generated by Django 3.1 on 2020-08-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200820_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='URL Slug'),
        ),
    ]