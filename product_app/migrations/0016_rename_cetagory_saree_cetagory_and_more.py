# Generated by Django 5.0.6 on 2024-10-31 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0015_alter_product_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cetagory',
            new_name='saree_cetagory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cetagory',
            new_name='saree_cetagory',
        ),
    ]