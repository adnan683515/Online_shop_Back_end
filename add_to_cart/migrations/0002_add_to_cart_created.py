# Generated by Django 5.0.6 on 2024-11-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_to_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_to_cart',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]