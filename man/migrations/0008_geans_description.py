# Generated by Django 5.1.2 on 2024-10-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0007_colour_of_geans_alter_geans_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='geans',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
