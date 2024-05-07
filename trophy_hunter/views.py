from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Game
import random

# Create your views here.


def index(request):
    all_games = list(Game.objects.all())
    random_game = random.sample(all_games, 5)[0]
    return render(
        request,
        "trophy_hunter/index.html",
        {
            "random_game": random_game
        }
    )


def error_400(request,  exception):
    """
    This function is getting the
    request and the exception if the
    request matches the error code,
    the template 400 will be shown
    """
    data = {}

    return render(request, 'trophy_hunter/400_csrf.html', data)


def error_403(request, exception):
    """
    This function is getting the
    request and the exception if the
    request matches the error code,
    the template 403 will be shown
    """
    data = {}

    return render(request, 'trophy_hunter/403_csrf.html', data)


def error_404(request,  exception):
    """
    This function is getting the
    request and the exception if the
    request matches the error code,
    the template 404 will be shown
    """
    data = {}

    return render(request, 'trophy_hunter/404_csrf.html', data)


def error_500(request):
    """
    This function is getting the
    request if the
    request matches the error code,
    the template 500 will be shown
    """
    data = {}

    return render(request, 'trophy_hunter/500_csrf.html', data)
