# Generated by Django 5.0.6 on 2024-10-29 02:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_remove_shirt_shirt_brand_remove_shirt_shirt_colour_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('rating', models.CharField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='review_geans',
            name='user',
        ),
        migrations.DeleteModel(
            name='type_of_shirt',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Brand',
        ),
        migrations.AddField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='review_geans',
        ),
    ]