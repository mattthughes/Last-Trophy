# Generated by Django 4.2.11 on 2024-03-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0009_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trophies',
            name='rarity',
            field=models.FloatField(default=55.13),
        ),
    ]