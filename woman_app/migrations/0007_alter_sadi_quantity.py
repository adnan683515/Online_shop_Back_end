# Generated by Django 5.0.6 on 2024-10-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woman_app', '0006_remove_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sadi',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
