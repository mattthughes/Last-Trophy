# Generated by Django 4.2.11 on 2024-03-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0010_alter_trophies_rarity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='game',
        ),
    ]
