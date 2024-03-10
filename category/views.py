from django.shortcuts import render,get_object_or_404, reverse
   
from django.views.generic.detail import DetailView
from trophy_hunter.models import Game,Trophies
from .filters import GameFilter
# Create your views here.

def game_list(request):
    game_filter = GameFilter(request.GET, queryset=Game.objects.all())
    context = {
        'form': game_filter.form,
        'games': game_filter.qs
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

class GameDetail(DetailView):
    # specify the model to use
    model = Game
    template_name = 'game_detail.html'

    


