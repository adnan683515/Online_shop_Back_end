# Generated by Django 5.0.6 on 2024-11-18 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0037_batsize_cricketbatbrand_mainmetariailsbat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='BatSize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.batsize'),
        ),
        migrations.AddField(
            model_name='product',
            name='CricketBatBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.cricketbatbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='MainMetariailsBat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.mainmetariailsbat'),
        ),
    ]