from django.shortcuts import render
from django.views import generic
from .models import Game

# Create your views here.
class GameList(generic.ListView):
    queryset = Game.objects.filter()
    template_name = "trophy_hunter/index.html"

def game_detail(DetailView):
    queryset = Game.objects.filter(title)
    game = get_object_or_404(queryset, slug=slug)

    return render
    (
        request, "trophy_hunter/game_detail.html",
    {
        "game": game,
        "trophies": trophies
    },
    )