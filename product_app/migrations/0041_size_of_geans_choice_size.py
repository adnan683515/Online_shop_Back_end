# Generated by Django 5.0.6 on 2024-11-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0040_brandofjacket_typeofjacket_warrentyofjacket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='size_of_geans',
            name='choice_size',
            field=models.CharField(blank=True, choices=[('JacketSize', 'JacketSize'), ('GeansSize', 'GeansSize')], max_length=100, null=True),
        ),
    ]