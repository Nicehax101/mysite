# Generated by Django 3.1 on 2020-08-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200820_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='title'),
        ),
    ]