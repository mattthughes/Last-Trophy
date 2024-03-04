from . import views
from django.urls import path

urlpatterns = [
    path("", views.GameList.as_view(), name='home'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    
]
