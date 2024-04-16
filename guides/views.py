from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.list import ListView 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from trophy_hunter.models import Trophies, Guide, Comment
from .forms import GuideForm, ApproveGuideForm
from django.http import HttpResponseRedirect

# Create your views here.

class GuideView(DetailView):
    model = Guide
    template_name = 'guide_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(GuideView, self).get_context_data(**kwargs)
        like = get_object_or_404(Guide, id=self.kwargs['pk'])
        dislike = get_object_or_404(Guide, id=self.kwargs['pk'])
        total_likes = like.total_likes()
        total_dislikes = dislike.total_dislikes()
        context['total_likes'] = total_likes
        context['total_dislikes'] = total_dislikes
        return context



def trophy_detail_view(request, slug):
    """
    This function is getting the user
    request and the trophy slug from the
    trophy model and is then returning this
    render showing the trophies and the guides
    of that trophy.
    """
    queryset = Trophies.objects.filter()
    trophies = get_object_or_404(queryset, slug=slug)
    game_guide = trophies.guides.filter(approved=True)
    guide_form = GuideForm()
    return render(
        request,
        "trophy_detail.html",
        {
            "trophies": trophies,
            "game_guide": game_guide,
            "guide_form": guide_form,
        },
    )

    

class AddGuideView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This class is using the create view to use
    the guide form created and put this on the
    webpage once the guide has been created a
    success message stating guide created is
    shown to give that feedback to the user.
    """
    model = Guide
    form_class = GuideForm
    success_message = 'Guide created awaiting approval'
    template_name = 'add_guide.html'

    """
    This function is redirecting the user to
    the trophy detail view, to determine which
    trophy the user was looking at the argument
    will be the trophy slug redirecting the user
    to the correct page.
    """

    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )

    """
    This function is checking to see if the
    form is valid by getting the trophy id
    as the primary key and the author as the

    """
    def form_valid(self, form):
        form.instance.trophy_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditGuideView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    This class is using the edit view to use
    the guide form created and put this on the
    webpage once the guide has been edited a
    success message stating guide edited is
    shown to give that feedback to the user.
    """
    model = Guide
    form_class = GuideForm
    success_message = 'Guide edited'
    template_name = 'edit_guide.html'

    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """
    def test_func(self):
        return self.request.user == self.get_object().author

    """
    This function is redirecting the user to
    the trophy detail view, to determine which
    trophy the user was looking at the argument
    will be the trophy slug redirecting the user
    to the correct page.
    """
    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )
    """
    This function is checking to see if the
    form is valid by getting the trophy id
    as the primary key and the author as the

    """

    def form_valid(self, form):
        form.instance.guide_id = self.kwargs['pk']
        return super().form_valid(form)


class DeleteGuide(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    This class is using the guide model
    with the template delete guide which
    will pop up when the user clicks delete
    guide after the guide has been deleted
    a pop up message stating guide deleted
    will appear on the page providing the
    user
    """
    model = Guide
    success_message = "Guide Deleted"
    template_name = 'delete_guide.html'

    """
    This function is redirecting the user to
    the trophy detail view, to determine which
    trophy the user was looking at the argument
    will be the trophy slug redirecting the user
    to the correct page.
    """

    def get_success_url(self):
        return reverse(
            'trophy-detail', kwargs={'slug': self.object.trophy.slug}
            )
    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """
    def test_func(self):
        return self.request.user == self.get_object().author


class GuideNotApproved(PermissionRequiredMixin, ListView):
    model = Guide
    template_name = 'guides_not_approved.html'
    permission_required = "approve_guide"

    def get_queryset(self, *args, **kwargs): 
        qs = super(GuideNotApproved, self).get_queryset(*args, **kwargs) 
        qs = qs.filter(approved=False)
        return qs
    
    def form_valid(self, form):
        return super().form_valid(form)


class GuideApproved(PermissionRequiredMixin, UpdateView):
    model = Guide
    form_class = ApproveGuideForm
    template_name = 'approve_guides.html'
    permission_required = "approve_guide"

    
    def get_success_url(self):
        return reverse(
            'not-approved-guide'
            )
    
    def form_valid(self, form):
        return super().form_valid(form)


def LikeView(request, pk):
    guide = get_object_or_404(Guide, id=request.POST.get('guide_id'))
    if request.user.is_authenticated and guide.likes:
        guide.likes.add(request.user)
    elif request.user.is_authenticated and guide.dislikes:
        guide.dislikes.add(request.user)
    else:
        return HttpResponseRedirect(reverse('account_login'))
    return HttpResponseRedirect(reverse('guide-view', args=[str(pk)]))


def DislikeView(request, pk):
    guide = get_object_or_404(Guide, id=request.POST.get('guide_id'))
    if request.user.is_authenticated:
        guide.dislikes.add(request.user)
    else:
        return HttpResponseRedirect(reverse('account_login'))
    return HttpResponseRedirect(reverse('guide-view', args=[str(pk)]))
    




