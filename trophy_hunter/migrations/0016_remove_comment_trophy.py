# Generated by Django 4.2.11 on 2024-04-16 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trophy_hunter', '0015_guide_dislikes_alter_guide_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='trophy',
        ),
    ]
