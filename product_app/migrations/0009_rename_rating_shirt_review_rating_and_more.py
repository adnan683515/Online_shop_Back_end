# Generated by Django 5.0.6 on 2024-10-29 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0008_remove_review_rating_review_football_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating_shirt',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_geans',
        ),
    ]