from django.shortcuts import render,get_object_or_404, reverse
from django.views.generic.edit import CreateView
from trophy_hunter.models import Trophies,Guide
from .forms import GuideForm

# Create your views here.

def guide_detail_view(request,slug):
    # specify the model to use
    queryset = Trophies.objects.filter()
    trophies = get_object_or_404(queryset, slug=slug)
    game_guide = trophies.guides.all()
    guide_form = GuideForm()
    

    return render(
        request,
        "guide_detail.html",
        {
            "trophies": trophies,
            "game_guide": game_guide,
            "guide_form": guide_form
            
        },
    )


def create_guide(request, slug, guide_id):
    """
    view to edit comments
    """

    queryset = Trophies.objects.filter()
    trophy = get_object_or_404(queryset, slug=slug)
    guide = get_object_or_404(Guide, pk=guide_id)
    guide_form = GuideForm(data=request.POST, instance=guide)
    
    return HttpResponseRedirect(reverse('guide_detail', args=[slug]))