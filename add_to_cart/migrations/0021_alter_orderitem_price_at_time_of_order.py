# Generated by Django 5.0.6 on 2024-11-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0020_alter_cartitem_cart_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price_at_time_of_order',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
