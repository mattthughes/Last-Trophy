# Generated by Django 4.2.11 on 2024-03-07 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('genre', models.CharField(choices=[('A', 'Action'), ('H', 'Horror'), ('R', 'Racing'), ('F', 'Fighting'), ('P', 'Platformer'), ('S', 'Stealth')], max_length=1)),
                ('trophy_count', models.CharField(max_length=4)),
                ('hours', models.CharField(max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
