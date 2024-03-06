from . import views
from django.urls import path

urlpatterns = [
    path("genre", views.GenresList.as_view(), name='genre'),
    path("game", views.GameList.as_view(), name="game"),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    
    
]