from . import views
from django.urls import path

urlpatterns = [
    path("", views.game_list, name='game'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    
    
]