from . import views
from django.urls import path
from .views import guide_detail_view

urlpatterns = [
    path('<slug:slug>/',views.guide_detail_view, name='trophy-detail'),
    path('<slug:slug>/create_guide/<int:guide_id>',
         views.create_guide, name='create_guide'),
    
]