from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from trophy_hunter.models import Game, Trophies
from .forms import GameForm
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


class AddGameView(SuccessMessageMixin, CreateView):
    """
    This class is using the create view to use
    the guide form created and put this on the
    webpage once the guide has been created a
    success message stating guide created is
    shown to give that feedback to the user.
    """
    model = Game
    form_class = GameForm
    success_message = 'Game Created'
    template_name = 'add_game.html'
    success_url = 'game'

    """
    This function is redirecting the user to
    the trophy detail view, to determine which
    trophy the user was looking at the argument
    will be the trophy slug redirecting the user
    to the correct page.
    """

    """
    This function is checking to see if the
    form is valid by getting the trophy id
    as the primary key and the author as the

    """
    def form_valid(self, form):
        return super().form_valid(form)