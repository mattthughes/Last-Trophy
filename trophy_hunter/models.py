from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    trophies = models.CharField(max_length=4)
    hours = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.title}"
    
class Trophies(models.Model):
    title = models.CharField(max_length=200, unique=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='achievements')
    author = models.ForeignKey(
            User, on_delete=models.CASCADE
        )
    description = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)
    rarity = models.CharField(max_length=10)

    class Meta:
        ordering = ["-rarity"]

    def __str__(self):
        return f" {self.title} {self.description}"
