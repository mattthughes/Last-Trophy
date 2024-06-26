"""
URL configuration for last_trophy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

handler404 = 'trophy_hunter.views.error_404'
handler403 = 'trophy_hunter.views.error_403'
handler400 = 'trophy_hunter.views.error_400'
handler500 = 'trophy_hunter.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("game", include("category.urls"), name="category-urls"),
    path("", include("trophy_hunter.urls"), name="trophy_hunter-urls"),
    path("guides", include("guides.urls"), name="guides-urls"),
    

]
