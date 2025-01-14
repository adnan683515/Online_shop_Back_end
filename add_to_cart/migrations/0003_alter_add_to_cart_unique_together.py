# Generated by Django 5.0.6 on 2024-11-02 06:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0002_add_to_cart_created'),
        ('product_app', '0022_delete_add_to_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='add_to_cart',
            unique_together={('user', 'Product')},
        ),
    ]
