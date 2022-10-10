from django.urls import path, include
from . import views

from main_app.views import Home

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('products_list/', views.ProductList.as_view(), name="products_list"),
    path('create/', views.Create.as_view(), name="create"),
    path('login/', views.Login.as_view(), name="login"),
    path('products/', views.Products.as_view(), name="products"),
    path('show/', views.Show.as_view(), name="show"),
    path('wishlist/', views.Wishlist.as_view(), name="wishlist"),
    path('cart/', views.Cart.as_view(), name="cart"),
]
