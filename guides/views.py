from django.shortcuts import render,get_object_or_404, reverse
from django.urls import reverse_lazy
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


class AddGuideView(CreateView):
    model = Guide
    form_class = GuideForm
    template_name = 'add_guide.html'
    success_url = reverse_lazy('game')

    def form_valid(self,form):
        form.instance.trophy_id = self.kwargs['pk']
        return super().form_valid(form)
