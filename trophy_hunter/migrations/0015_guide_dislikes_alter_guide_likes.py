# Generated by Django 4.2.11 on 2024-04-16 08:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trophy_hunter', '0014_guide_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='dislikes',
            field=models.ManyToManyField(related_name='guide_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='guide',
            name='likes',
            field=models.ManyToManyField(related_name='guide_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]