from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Game(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'A'
        HORROR = 'H'
        RACING = 'R'
        FIGHTING = 'F'
        PLATFORMER = 'P'
        STEALTH = 'S'
        
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    featured_image = CloudinaryField('image', default='placeholder')
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    trophy_count = models.CharField(max_length=4)
    hours = models.CharField(max_length=4)
    game_score = models.IntegerField(default=1000)
    rating = models.FloatField(default=4.99)

    def __str__(self):
        return f" {self.title}"
    

class Trophies(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, default="trop-slug")
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='trophies')
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)
    rarity = models.FloatField(default=55.13)

    class Meta:
        ordering = ["-rarity"]

    def __str__(self):
        return f" {self.title} {self.description}"


class Guide(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    trophy = models.ForeignKey(
        Trophies, on_delete=models.CASCADE, related_name='guides'
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.body} {self.author}"


