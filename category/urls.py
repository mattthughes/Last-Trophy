from . import views
from django.urls import path
from .views import GameDetail


urlpatterns = [
    path("", views.game_list, name='game'),
    path('<slug:slug>/',GameDetail.as_view(), name='game-detail')
    
    
]