from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Products
# This will import the class we are extending 
from django.views.generic.edit import CreateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"


#...
class About(TemplateView):
    template_name = "about.html"


class ProductCreate(CreateView):
    model = Products
    fields = ['name', 'img', 'bio']
    template_name = "product_create.html"

    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        # form.instance = {
            # name: Baby Shark 2,
            # img: my image url,
            # Bio: Some string
        # }
        form.instance.user = self.request.user
        # form.instance = {
            # name: Another Test,
            # img: a.com,
            # Bio: Proving a point,
            # user: self.request.user
        # }
        # form.instance.verified_artist = False
        return super(ProductCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('artist_detail', kwargs={'pk': self.object.pk})


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
        name = self.request.GET.get("name")
        if name != None:
            context["products"] = Products.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["products"] = Products.objects.all()
            # default header for not searching 
            context["header"] = f"Searching for {name}"
        return context

