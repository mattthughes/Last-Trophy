from django.urls import path
from . import views
from .views import guide_detail_view, AddGuideView, EditGuideView, DeleteGuide

urlpatterns = [
    path('<slug:slug>/', views.guide_detail_view, name='trophy-detail'),
    path('<int:pk>/create/', AddGuideView.as_view(), name='create-guide'),
    path('<int:pk>/edit/', EditGuideView.as_view(), name='edit-guide'),
    path('<int:pk>/delete/', DeleteGuide.as_view(), name='delete-guide')

]
