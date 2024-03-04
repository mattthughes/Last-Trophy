from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Game, Trophy

# Create your views here.
class GameList(generic.ListView):
    queryset = Game.objects.filter()
    template_name = "trophy_hunter/index.html"


def game_detail(request, slug):
    queryset = Game.objects.filter()
    game = get_object_or_404(queryset, slug=slug)
    trophies = game.trophies.all().order_by("-rarity")

    return render(
        request,
        "trophy_hunter/game_detail.html",
        {
            "game": game,
            "trophies": trophies,
            
        },
    )
