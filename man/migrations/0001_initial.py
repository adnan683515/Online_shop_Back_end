# Generated by Django 5.1.2 on 2024-10-27 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='geans_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='geans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geans_name', models.CharField(max_length=100)),
                ('geans_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man.geans_size')),
            ],
        ),
    ]