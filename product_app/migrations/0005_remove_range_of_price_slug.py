# Generated by Django 5.0.6 on 2024-10-29 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_rename_range_geans_price_range_of_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='range_of_price',
            name='slug',
        ),
    ]
