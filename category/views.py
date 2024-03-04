from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from trophy_hunter.models import Categories, Game, Trophy
from itertools import chain
# Create your views here.


class CategoryList(generic.ListView):
    queryset = Categories.objects.filter()
    template_name = "category.html"

def category_detail(request, slug):
    queryset = Categories.objects.filter()
    categories = get_object_or_404(queryset, slug=slug)
    games = Game.objects.all()
    trophies = Trophy.objects.all()

    return render(
        request,
        "category_detail.html",
        {
            "categories": categories,
            "games": games,
            "trophies": trophies

        },
    )


