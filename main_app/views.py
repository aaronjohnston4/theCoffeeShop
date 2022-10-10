from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

    # Here we are adding a method that will be run when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("The Coffee Shop Home")


#...
class About(TemplateView):
    template_name = "about.html"


class Create(TemplateView):
    template_name = "create.html"


class Products(TemplateView):
    template_name = "products.html"


class Show(TemplateView):
    template_name = "show.html"


class Login(TemplateView):
    template_name = "login.html"


class Wishlist(TemplateView):
    template_name = "wishlist.html"


class Cart(TemplateView):
    template_name = "cart.html"
