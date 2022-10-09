from django.urls import path, include
from . import views

from main_app.views import Home

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]
