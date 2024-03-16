from . import views
from django.urls import path
from .views import game_detail_view


urlpatterns = [
    path("", views.game_list, name='game'),
    path('<slug:slug>/',views.game_detail_view, name='game-detail'),
    
    
    
]