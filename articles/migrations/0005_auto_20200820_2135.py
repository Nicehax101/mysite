# Generated by Django 3.1 on 2020-08-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200820_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(),
        ),
    ]