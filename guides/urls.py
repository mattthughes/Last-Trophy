from . import views
from django.urls import path
from .views import guide_detail_view, AddGuideView

urlpatterns = [
    path('<slug:slug>/',views.guide_detail_view, name='trophy-detail'),
    path('<int:pk>/create', AddGuideView.as_view(), name='create-view')
    
]