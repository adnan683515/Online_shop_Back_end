# Generated by Django 5.0.6 on 2024-11-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0042_delete_warrentyofjacket_product_brandofjacket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmetariailsbat',
            name='choice_option',
            field=models.CharField(blank=True, choices=[('jacket', 'jacket'), ('Bat', 'Bat')], max_length=100, null=True),
        ),
    ]