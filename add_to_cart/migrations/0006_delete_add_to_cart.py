# Generated by Django 5.0.6 on 2024-11-04 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0005_alter_add_to_cart_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ADD_TO_CART',
        ),
    ]