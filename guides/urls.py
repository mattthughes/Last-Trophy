from . import views
from django.urls import path
from .views import guide_detail_view

urlpatterns = [
    path('<slug:slug>/',views.guide_detail_view, name='trophy-detail'),
    
]