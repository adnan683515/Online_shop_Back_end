# Generated by Django 5.0.6 on 2024-12-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0030_order_upzila_order_zila'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20),
        ),
    ]
