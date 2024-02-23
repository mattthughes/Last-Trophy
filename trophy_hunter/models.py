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


