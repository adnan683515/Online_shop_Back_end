# Generated by Django 5.0.6 on 2024-12-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0061_alter_cetagory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='size_number',
        ),
        migrations.AlterField(
            model_name='size',
            name='choice_size',
            field=models.CharField(blank=True, choices=[('Geans', 'Geans'), ('Saree', 'Saree'), ('Jacket', 'Jacket'), ('Watch', 'Watch'), ('Bat Size', 'Bat Size')], max_length=100, null=True),
        ),
    ]
