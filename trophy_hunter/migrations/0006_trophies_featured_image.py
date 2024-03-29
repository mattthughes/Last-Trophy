# Generated by Django 4.2.11 on 2024-03-10 18:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0005_game_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trophies',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
