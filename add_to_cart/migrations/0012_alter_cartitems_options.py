# Generated by Django 5.0.6 on 2024-11-13 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0011_cartitems_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'ordering': ['date']},
        ),
    ]