from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from trophy_hunter.models import Game
from .filters import GameFilter
# Create your views here.

def game_list(request):
    game_filter = GameFilter(request.GET, queryset=Game.objects.all())
    context = {
        'form': game_filter.form,
        'game': game_filter.qs
    }
    return render(request, 'category.html', context)

#def GameList(request):
    #genre = request.GET.get('action')
    #game = Games.objects.all()
    #if genre:
        #game = game.filter(genre_icontains=genre)
    #context = {
        #'genre': genre,
        #'game': game
    #}
    #return render(request, 'game.html', context)


def game_detail(request, slug):
    game = get_object_or_404(queryset, slug=slug)
    trophies = game.trophies.all().order_by("-rarity")

    return render(
        request,
        "game_detail.html",
        {
            
            "game": game,
            "trophies": trophies
            
        },
    )

