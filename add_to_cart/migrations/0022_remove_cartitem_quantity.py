# Generated by Django 5.0.6 on 2024-11-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0021_alter_orderitem_price_at_time_of_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
