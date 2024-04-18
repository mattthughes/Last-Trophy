from django.urls import path
from . import views
from .views import (
    trophy_detail_view,
    AddGuideView,
    EditGuideView,
    DeleteGuide,
    GuideNotApproved,
    GuideApproved,
    LikeView,
    DislikeView,
    GuideView,
    AddComment,
    EditComment,
    DeleteComment,
    AdminListGuides,
    AdminDeleteGuide,
    AdminCommentList,
    AdminCommentDelete
    )

urlpatterns = [
    path('<slug:slug>/', views.trophy_detail_view, name='trophy-detail'),
    path(
        '/guide/not-approved',
        GuideNotApproved.as_view(), name='not-approved-guide'
        ),
    path('/<int:pk>/approve', GuideApproved.as_view(), name='approve-guide'),
    path('/guides/list', AdminListGuides.as_view(), name='guides-list'),
    path('<int:pk>/guides/list/delete/', AdminDeleteGuide.as_view(), name='delete-guide-list'),
    path('/comments/list', AdminCommentList.as_view(), name='comments-list'),
    path('<int:pk>/comments/list/delete/', AdminCommentDelete.as_view(), name='delete-comment-list'),
    path('<int:pk>/create/', AddGuideView.as_view(), name='create-guide'),
    path('<int:pk>/edit/', EditGuideView.as_view(), name='edit-guide'),
    path('<int:pk>/delete/', DeleteGuide.as_view(), name='delete-guide'),
    path('<int:pk>/guides', GuideView.as_view(), name='guide-view'),
    path('like/<int:pk>', views.LikeView, name='like-guide'),
    path('dislike/<int:pk>', views.DislikeView, name='dislike-guide'),
    path('<int:pk>/Add/Comment/', AddComment.as_view(), name='add-comment'),
    path('<int:pk>/Edit/', EditComment.as_view(), name='edit-comment'),
    path(
        '<int:pk>/Delete/Comment/',
        DeleteComment.as_view(), name='delete-comment'
        )
]
