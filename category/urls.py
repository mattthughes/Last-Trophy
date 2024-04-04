from . import views
from django.urls import path
from .views import game_detail_view, AddGameView


urlpatterns = [
    path("/", views.game_list, name='game'),
    path('/<slug:slug>', views.game_detail_view, name='game-detail'),
    path('/add/game', AddGameView.as_view(), name='add-game'),
]
