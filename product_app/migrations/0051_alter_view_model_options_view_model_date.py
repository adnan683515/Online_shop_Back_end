# Generated by Django 5.0.6 on 2024-12-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0050_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='view_model',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='view_model',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
