# Generated by Django 4.2.11 on 2024-03-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0008_game_game_score_alter_guide_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.FloatField(default=4.99),
        ),
    ]
