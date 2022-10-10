from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"


#...
class About(TemplateView):
    template_name = "about.html"


class Create(TemplateView):
    template_name = "create.html"


class Products:

    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


class Show(TemplateView):
    template_name = "show.html"


class Login(TemplateView):
    template_name = "login.html"


class Wishlist(TemplateView):
    template_name = "wishlist.html"


class Cart(TemplateView):
    template_name = "cart.html"


class ProductList(TemplateView):
    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products # this is where we add the key into our context object for the view to use
        return context



