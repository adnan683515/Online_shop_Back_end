# Generated by Django 5.0.6 on 2024-12-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0034_order_oderdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='end_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
