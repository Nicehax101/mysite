# Generated by Django 3.1 on 2020-08-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200820_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='myslug()', unique=True, verbose_name='URL Slug'),
        ),
    ]
