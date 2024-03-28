from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from trophy_hunter.models import Trophies, Guide
from .forms import GuideForm

# Create your views here.


def guide_detail_view(request, slug):
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


class AddGuideView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Guide
    form_class = GuideForm
    success_message = 'Guide created'
    template_name = 'add_guide.html'

    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )

    def form_valid(self, form):
        form.instance.trophy_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class EditGuideView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Guide
    form_class = GuideForm
    success_message = 'Guide edited'
    template_name = 'edit_guide.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    
    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )

    def form_valid(self, form):
        form.instance.guide_id = self.kwargs['pk']
        return super().form_valid(form)
    


class DeleteGuide(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Guide
    success_message = "Guide Deleted"
    template_name = 'delete_guide.html'

    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )
        
    def test_func(self):
        return self.request.user == self.get_object().author
