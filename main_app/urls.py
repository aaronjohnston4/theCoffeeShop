from django.urls import path, include
from . import views

from main_app.views import Home

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductList.as_view(), name="products_list"),
    path('products/new/', views.ProductCreate.as_view(), name="product_create"),
    path('login/', views.Login.as_view(), name="login"),
    path('show/', views.Show.as_view(), name="show"),
    path('wishlist/', views.Wishlist.as_view(), name="wishlist"),
    path('cart/', views.Cart.as_view(), name="cart"),
]
