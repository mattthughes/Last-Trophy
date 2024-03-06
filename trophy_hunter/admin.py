from django.contrib import admin
from .models import Game, Trophy, Genres, Categories
# Register your models here.
admin.site.register(Game)
admin.site.register(Trophy)
admin.site.register(Genres)
admin.site.register(Categories)