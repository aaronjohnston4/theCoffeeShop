from django.shortcuts import redirect, render
from django.views import View # <- View class to handle requests

#...
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Products
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"


#...
class About(TemplateView):
    template_name = "about.html"


class ProductCreate(CreateView):
    model = Products
    fields = ['name', 'img', 'bio', 'verified_products']
    template_name = "product_create.html"
    success_url = "/products/"
    # This is our new method that will add the user into our submitted form
    # def form_valid(self, form):
    #     # form.instance = {
    #         # name: Baby Shark 2,
    #         # img: my image url,
    #         # Bio: Some string
    #     # }
    #     form.instance.user = self.request.user
    #     # form.instance = {
    #         # name: Another Test,
    #         # img: a.com,
    #         # Bio: Proving a point,
    #         # user: self.request.user
    #     # }
    #     # form.instance.verified_artist = False
    #     return super(ProductCreate, self).form_valid(form)

    # def get_success_url(self):
    #     print(self.kwargs)
    #     return reverse('product_detail', kwargs={'pk': self.object.pk})


# class Products:

#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


class ProductDetail(DetailView):
    model = Products
    template_name = "product_detail.html"


class ProductUpdate(UpdateView):
    model = Products
    fields = ['name', 'img', 'bio', 'verified_products']
    template_name = "product_update.html"
    success_url = "/products/"

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    model = Products
    template_name = "product_delete.html"
    success_url = "/products/"


class Login(TemplateView):
    template_name = "login.html"


class Wishlist(TemplateView):
    template_name = "wishlist.html"


class Cart(TemplateView):
    template_name = "cart.html"


class ProductList(TemplateView):
    template_name = "products_list.html"
#     In here, I want to check if there has been a query made
# I know the queries will have a key of name
# const context = {
#     artists: //finding ArtistList,
#     stuff_at_top: "This is a string"
# }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mySearchName = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if mySearchName != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["products"] = Products.objects.filter(name__icontains=mySearchName)
            context["stuff_at_top"] = f"Searching through Products list for {mySearchName}"
        else:
            context["products"] = Products.objects.filter()
            context["stuff_at_top"] = "Trending Products"
        return context
