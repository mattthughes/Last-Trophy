from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    trophy_count = models.CharField(max_length=4)
    hours = models.CharField(max_length=4)
    genre = models.CharField(max_length=200, unique=True, default='action')

    def __str__(self):
        return f"{self.title}"
    

class Trophy(models.Model):
    title = models.CharField(max_length=200, unique=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='trophies')
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

class Genre(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Categories(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name="categories"
    )
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.genre} {self.game}"
    