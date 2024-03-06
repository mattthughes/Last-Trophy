from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from trophy_hunter.models import Game, Trophy, Categories, Genres
from itertools import chain
# Create your views here.
    
class GenresList(generic.ListView):
    queryset = Genres.objects.filter()
    template_name = "category.html"

class GameList(generic.ListView):
    queryset = Game.objects.filter()
    template_name = "game.html"

def game_detail(request, slug):
    queryset = Game.objects.filter()
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



