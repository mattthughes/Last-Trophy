from django.shortcuts import render,get_object_or_404, reverse
from trophy_hunter.models import Trophies,Guide

# Create your views here.

def guide_detail_view(request,slug):
    # specify the model to use
    queryset = Trophies.objects.filter()
    trophies = get_object_or_404(queryset, slug=slug)
    game_guide = trophies.guides.all()
    

    return render(
        request,
        "guide_detail.html",
        {
            "trophies": trophies,
            "game_guide": game_guide
            
        },
    )
