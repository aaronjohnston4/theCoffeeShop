from django.urls import path, include
from . import views

from main_app.views import Home

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('create/', views.About.as_view(), name="about"),
    path('login/', views.About.as_view(), name="about"),
    path('products/', views.About.as_view(), name="about"),
    path('show/', views.About.as_view(), name="about"),
    path('wishlist/', views.About.as_view(), name="about"),
]
