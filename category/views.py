from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from itertools import chain
from trophy_hunter.models import Genre, Games
# Create your views here.

class GenresList(generic.ListView):
    queryset = Genre.objects.filter("title")
    template_name = "category.html"    

class GameList(generic.ListView):
    queryset = Games.objects.filter()
    template_name = "game.html"

def game_detail(request, slug):
    queryset = Games.objects.filter()
    game = get_object_or_404(queryset, slug=slug)
    trophies = game.trophies.all().order_by("-rarity")

    return render(
        request,
        "game_detail.html",
        {
            "game": game,
            "trophies": trophies,
            
        },
    )



