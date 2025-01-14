# Generated by Django 5.0.6 on 2024-10-28 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0012_geans_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='range_geans_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='geans',
            name='geans_price',
        ),
        migrations.AddField(
            model_name='geans',
            name='fixed_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='geans',
            name='range_geans_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='man.range_geans_price'),
        ),
        migrations.DeleteModel(
            name='geans_price',
        ),
    ]
