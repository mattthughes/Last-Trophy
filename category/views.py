from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.detail import DetailView
from trophy_hunter.models import Game, Trophies
from .filters import GameFilter
# Create your views here.


def game_list(request):
    game_filter = GameFilter(request.GET, queryset=Game.objects.all())
    context = {
        'form': game_filter.form,
        'games': game_filter.qs
    }
    return render(request, 'category.html', context)


def game_detail_view(request, slug):
    # specify the model to use
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
