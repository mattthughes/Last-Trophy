from . import views
from django.urls import path

urlpatterns = [
    path("", views.game_list, name='category'),
    #path("game", views.GameList, name="game"),
    #path('<slug:slug>/', views.game_detail, name='game_detail'),
    
    
]