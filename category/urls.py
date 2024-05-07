from . import views
from django.urls import path
from .views import (
    game_detail_view,
    AddGameView,
    EditGameView,
    DeleteGame,
    AddTrophyView,
    EditTrophyView,
    DeleteTrophyView)


urlpatterns = [
    path("/", views.game_list, name='game'),
    path('/<slug:slug>/', views.game_detail_view, name='game-detail'),
    path('/add/game/', AddGameView.as_view(), name='add-game'),
    path('/<slug:slug>/edit/', EditGameView.as_view(), name='edit-game'),
    path(
        '/<slug:slug>/delete/game/', DeleteGame.as_view(), name='delete-game'
        ),
    path('/<int:pk>/create/', AddTrophyView.as_view(), name='add-trophy'),
    path(
        '/<slug:slug>/edit/trophy/',
        EditTrophyView.as_view(), name='edit-trophy'
        ),
    path(
        '/<slug:slug>/delete/trophy/',
        DeleteTrophyView.as_view(), name='delete-trophy'
        )
]
