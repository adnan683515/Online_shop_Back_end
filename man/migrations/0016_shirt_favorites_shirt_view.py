# Generated by Django 5.0.6 on 2024-10-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0015_shirt_brand_shirt_colour_shirt_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='favorites',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shirt',
            name='view',
            field=models.BooleanField(default=False),
        ),
    ]
