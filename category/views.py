from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.detail import DetailView
from trophy_hunter.models import Game, Trophies
from .filters import GameFilter
# Create your views here.


def game_list(request):
    """
    This function is taking a request which is
    get and is quereing the game data model,
    setting the form as the game filter form
    and the game as the filtered querey set
    then returing the request, the template
    category which is the template and the context.
    """
    game_filter = GameFilter(request.GET, queryset=Game.objects.all())
    context = {
        'form': game_filter.form,
        'games': game_filter.qs
    }
    return render(request, 'category.html', context)


def game_detail_view(request, slug):
    """
    This function is getting the request,
    the slug the queryset is the game model
    which will show the fields of the game
    model. The function is returing the game
    model and the trophies which is a foreign
    key of the game model.
    """
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
