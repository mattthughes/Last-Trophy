# Generated by Django 4.2.11 on 2024-03-07 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0002_game_delete_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=200)),
                ('rarity', models.CharField(max_length=10)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trophies', to='trophy_hunter.game')),
            ],
            options={
                'ordering': ['-rarity'],
            },
        ),
    ]
