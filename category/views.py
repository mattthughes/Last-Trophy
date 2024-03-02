from django.shortcuts import render
from django.views import generic
from trophy_hunter.models import Categories
# Create your views here.

def CategoryList(request):
    categories = Categories.objects.all()

    return render(
        request,
        "category.html",
        {
            "categories": categories,
        },
    )
