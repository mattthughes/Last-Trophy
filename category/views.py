from django.shortcuts import render
from django.views import generic
from trophy_hunter.models import Categories
# Create your views here.

def CategoryList(request):
    categories = Categories.objects.all().order_by("-genre")

    return render(
        request,
        "trophy_hunter/test.html",
        {
            "categories": categories,
        },
    )
