# Generated by Django 5.0.6 on 2024-10-28 05:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ball_colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('view', models.BooleanField(default=False)),
                ('favorites', models.BooleanField(default=False)),
                ('ball_colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.ball_colour')),
            ],
        ),
        migrations.CreateModel(
            name='review_football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('rating', models.CharField(choices=[('⚽', '⚽'), ('⚽⚽', '⚽⚽'), ('⚽⚽⚽', '⚽⚽⚽'), ('⚽⚽⚽⚽', '⚽⚽⚽⚽'), ('⚽⚽⚽⚽⚽', '⚽⚽⚽⚽⚽')], max_length=100)),
                ('Ball', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.ball')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]