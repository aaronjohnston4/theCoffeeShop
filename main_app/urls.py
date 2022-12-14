from django.urls import path, include
from . import views

from main_app.views import Home

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductList.as_view(), name="products_list"),
    path('products/new/', views.ProductCreate.as_view(), name="product_create"),
    path('accounts/login/', views.Login.as_view(), name="login"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    path('wishlist/', views.Wishlists.as_view(), name="wishlist"),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('products/<int:pk>/update',views.ProductUpdate.as_view(), name="product_update"),
    path('products/<int:pk>/delete',views.ProductDelete.as_view(), name="product_delete"),
    path('products/<int:pk>/sizes/new/', views.SizeCreate.as_view(), name="size_create"),
    path('wishlist/<int:pk>/product/<int:product_pk>/', views.WishlistProductAssoc.as_view(), name="wishlist_product_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
