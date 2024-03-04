from . import views
from django.urls import path

urlpatterns = [
    path("", views.CategoryList.as_view(), name='category'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    
    
]