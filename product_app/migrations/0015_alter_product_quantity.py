# Generated by Django 5.0.6 on 2024-10-30 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0014_remove_product_view_view_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]