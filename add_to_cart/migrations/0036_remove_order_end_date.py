# Generated by Django 5.0.6 on 2024-12-23 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0035_remove_order_created_at_order_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='end_date',
        ),
    ]
