from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from trophy_hunter.models import Game, Trophy, Category
from itertools import chain
# Create your views here.


class CategoryList(generic.ListView):
    queryset = Category.objects.filter()
    template_name = "category.html"

def category_detail(request, slug):
    queryset = Category.objects.filter()
    categories = get_object_or_404(queryset, slug=slug)
    game = Game.objects.all()
    trophies = Trophy.objects.all()

    return render(
        request,
        "category_detail.html",
        {
            "categories": categories,
            "game": game,
            "trophies": trophies

        },
    )


