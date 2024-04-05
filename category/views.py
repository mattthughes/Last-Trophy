from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from trophy_hunter.models import Game, Trophies
from .forms import GameForm, TrophiesForm
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


class AddGameView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This class is using the create view to use
    the game form created and put this on the
    webpage once the game has been created a
    success message stating game created is
    shown to give that feedback to the user.
    """
    model = Game
    form_class = GameForm
    success_message = 'Game Created'
    template_name = 'add_game.html'
    permission_required = "add_game"

    """
    This function is redirecting the user to
    the game view.
    """
    def get_success_url(self):
        return reverse(
            'game'
            )

    def test_func(self):
        return self.request.user == self.get_object().author

    """
    This function is checking to see if the
    form is valid by getting the trophy id
    as the primary key and the author as the

    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditGameView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    This class is using the edit view to use
    the game form created and put this on the
    webpage once the game has been edited a
    success message stating game edited is
    shown to give that feedback to the user.
    """
    model = Game
    form_class = GameForm
    success_message = 'Game edited'
    template_name = 'edit_game.html'

    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """
    def test_func(self):
        return self.request.user == self.get_object().author

    """
    This function is redirecting the user to
    the game view.
    """
    def get_success_url(self):
        return reverse(
            'game'
            )
    """
    This function is checking to see if the
    form is valid.
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteGame(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    This class is using the game model
    with the template delete game which
    will pop up when the user clicks delete
    game after the game has been deleted
    a pop up message stating guide deleted
    will appear on the page providing the
    user with this feedback.
    """
    model = Game
    success_message = "Game Deleted"
    template_name = 'delete_game.html'
    success_message = 'Game Deleted'

    """
    This function is redirecting the user to
    the game view
    """
    def get_success_url(self):
        return reverse(
            'game'
            )
    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """
    def test_func(self):
        return self.request.user == self.get_object().author


class AddTrophyView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This class is using the create view to use
    the trophies form created and put this on the
    webpage once the trophy has been created a
    success message stating trophy created is
    shown to give that feedback to the user.
    """
    model = Trophies
    form_class = TrophiesForm
    success_message = 'Trophy Created'
    template_name = 'add_trophy.html'
    permission_required = "add_trophies"

    """
    This function is redirecting the user to
    the game detail view.
    """
    def get_success_url(self):
        return reverse(
            'game-detail', kwargs={'slug': self.object.game.slug}
            )

    def test_func(self):
        return self.request.user == self.get_object().author

    """
    This function is checking to see if the
    form is valid by setting the author
    to the user that clicked on the create button.
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditTrophyView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This class is using the edit view to use
    the game form created and put this on the
    webpage once the game has been edited a
    success message stating game edited is
    shown to give that feedback to the user.
    """
    model = Trophies
    form_class = TrophiesForm
    success_message = 'Trophy edited'
    template_name = 'edit_trophy.html'
    permission_required = "edit_trophies"


    """
    This function is redirecting the user to
    the game detail view.
    """
    def get_success_url(self):
        return reverse(
            'game-detail', kwargs={'slug': self.object.game.slug}
            )
    """
    This function is checking to see if the
    form is valid.
    """
    def form_valid(self, form):
        return super().form_valid(form)
