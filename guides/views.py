from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from trophy_hunter.models import Trophies, Guide, Comment
from .forms import GuideForm, ApproveGuideForm, CommentForm
from django.http import HttpResponseRedirect

# Create your views here.

class LastTrophyPermissions(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        if self.request.user.is_superuser:
            return self.get_object().author
        else:
            return self.request.user == self.get_object().author
class GuideView(DetailView):
    """
    This class is using the detail view to show
    one guide per page where the user can
    add likes and dislikes to a specific
    guide.
    """
    model = Guide
    template_name = 'guide_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(GuideView, self).get_context_data(**kwargs)
        like = get_object_or_404(Guide, id=self.kwargs['pk'])
        dislike = get_object_or_404(Guide, id=self.kwargs['pk'])
        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = like.total_likes()
        total_dislikes = dislike.total_dislikes()
        context['total_likes'] = total_likes
        context['total_dislikes'] = total_dislikes
        context["liked"] = liked
        return context

class GuideNotApproved(PermissionRequiredMixin, ListView):
    """
    This class is showcasing the guides which are not approved
    in a list only the admin user will be able to view this page
    which will be controlled by the permission required mixin.
    """
    model = Guide
    template_name = 'guides_not_approved.html'
    permission_required = "approve_guide"


    def get_queryset(self, *args, **kwargs):
        qs = super(GuideNotApproved, self).get_queryset(*args, **kwargs)
        qs = qs.filter(approved=False)
        return qs

    def form_valid(self, form):
        return super().form_valid(form)


class GuideApproved(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This class is using the form approve guide form to
    allow the admin user to approve guides which are
    awaiting approval this will be controlled by the
    permission required mixin once the guide has been
    approved the success url will return the guides
    awaiting approval page.
    """
    model = Guide
    form_class = ApproveGuideForm
    success_message = 'Approved'
    template_name = 'approve_guides.html'
    permission_required = "approve_guide"
    
    

    def get_success_url(self):
        return reverse(
            'not-approved-guide'
            )

    def form_valid(self, form):
        return super().form_valid(form)


class AdminListGuides(PermissionRequiredMixin, ListView):
    """
    This class is showcasing the guides which are not approved
    in a list only the admin user will be able to view this page
    which will be controlled by the permission required mixin.
    """
    model = Guide
    template_name = 'admin_guides.html'
    permission_required = "delete_guide"

    def form_valid(self, form):
        return super().form_valid(form)


class AdminDeleteGuide(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    This class is using the guide model
    with the template delete guide which
    will pop up when the user clicks delete
    guide after the guide has been deleted
    a pop up message stating guide deleted
    will appear on the page.
    """
    model = Guide
    success_message = "Guide Deleted"
    template_name = 'delete_guide.html'
    permission_required = "delete_guide"

    """
    This function is redirecting the admin user to
    the guide list.
    """

    def get_success_url(self):
        return reverse(
            'guides-list'
            )

class GuideNotApproved(PermissionRequiredMixin, SuccessMessageMixin, ListView):
    """
    This class is showcasing the guides which are not approved
    in a list only the admin user will be able to view this page
    which will be controlled by the permission required mixin.
    """
    model = Guide
    template_name = 'guides_not_approved.html'
    permission_required = "approve_guides"
    success_message = 'Guide Approved'

    def get_queryset(self, *args, **kwargs):
        qs = super(GuideNotApproved, self).get_queryset(*args, **kwargs)
        qs = qs.filter(approved=False)
        return qs

    def form_valid(self, form):
        return super().form_valid(form)


class AdminCommentList(PermissionRequiredMixin, ListView):
    """
    This class is showcasing the guides which are not approved
    in a list only the admin user will be able to view this page
    which will be controlled by the permission required mixin.
    """
    model = Comment
    template_name = 'admin_comments.html'
    permission_required = "delete_comment"

    def form_valid(self, form):
        return super().form_valid(form)


class AdminCommentDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    This class is using the comment model
    with the template delete comment which
    will pop up when the user clicks delete
    comment after the comment has been deleted
    a pop up message stating comment deleted
    will appear on the page.
    """
    model = Comment
    success_message = "Comment Deleted"
    template_name = 'delete_comment.html'
    permission_required = "delete_comment"

    """
    This function is redirecting the admin user to
    the guide list.
    """

    def get_success_url(self):
        return reverse(
            'comments-list'
            )


class AddComment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_message = 'Comment created'

    def get_success_url(self):
        return reverse(
            'guide-view', kwargs={'pk': self.object.guide.pk}
            )

    """
    This function is checking to see if the
    form is valid by getting the trophy id
    as the primary key and the author as the

    """
    def form_valid(self, form):
        form.instance.guide_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditComment(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    This class is using the edit view to use
    the Comment form created and put this on the
    webpage once the Comment has been edited a
    success message stating Comment edited is
    shown to give that feedback to the user.
    """
    model = Comment
    form_class = CommentForm
    success_message = 'Comment edited'
    template_name = 'edit_comment.html'

    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """
    def test_func(self):
        return self.request.user == self.get_object().author

    """
    This function is redirecting the user to
    the guide view, to determine which
    guide the user was looking at the argument
    will be the guide pk redirecting the user
    to the correct page.
    """
    def get_success_url(self):
        return reverse(
            'guide-view', kwargs={'pk': self.object.guide.pk}
            )
    """
    This function is checking to see if the
    form is valid by getting the comment id
    as the primary key.

    """

    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)


class DeleteComment(LastTrophyPermissions, SuccessMessageMixin, DeleteView):
    """
    This class is using the Comment model
    with the template delete Comment which
    will pop up when the user clicks delete
    Comment after the Comment has been deleted
    a pop up message stating Comment deleted
    will appear on the page providing the
    user
    """
    model = Comment
    success_message = "Comment Deleted"
    template_name = 'delete_comment.html'

    """
    This function is redirecting the user to
    the guide view, to determine which
    guide the user was looking at the argument
    will be the guide pk redirecting the user
    to the correct page.
    """

    def get_success_url(self):
        return reverse(
            'guide-view', kwargs={'pk': self.object.guide.pk}
            )
    """
    This function is making sure the
    user making the request is the user
    logged in otherwise show a 403 error
    """


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


class DeleteGuide(LastTrophyPermissions, SuccessMessageMixin, DeleteView):
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


class GuideApproved(PermissionRequiredMixin, UpdateView):
    """
    This class is using the form approve guide form to
    allow the admin user to approve guides which are
    awaiting approval this will be controlled by the
    permission required mixin once the guide has been
    approved the success url will return the guides
    awaiting approval page.
    """
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
    """
    This function is getting the guides id and is then checking if
    the user is authenticated if they are to add on the likes attribute
    to this specific guide. if the user is not logged in to redirect the
    user to the login page.
    """
    guide = get_object_or_404(Guide, id=request.POST.get('guide_id'))
    liked = False
    if guide.likes.filter(id=request.user.id).exists():
        guide.likes.remove(request.user)
        liked = False
    elif request.user.is_authenticated:
        guide.likes.add(request.user)
        liked = True
    else:
        return HttpResponseRedirect(reverse('account_login'))
    return HttpResponseRedirect(reverse('guide-view', args=[str(pk)]))


def DislikeView(request, pk):
    """
    This function is getting the guides id and is then checking if
    the user is authenticated if they are to add on the dislikes attribute
    to this specific guide. if the user is not logged in to redirect the
    user to the login page.
    """
    guide = get_object_or_404(Guide, id=request.POST.get('guide_id'))
    if request.user.is_authenticated:
        guide.dislikes.add(request.user)
    else:
        return HttpResponseRedirect(reverse('account_login'))
    return HttpResponseRedirect(reverse('guide-view', args=[str(pk)]))