# Generated by Django 5.0.6 on 2024-12-23 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0032_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
    ]