# Generated by Django 5.0.6 on 2024-11-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0003_alter_add_to_cart_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_to_cart',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]