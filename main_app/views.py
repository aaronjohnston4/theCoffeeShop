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


class Products(TemplateView):
    template_name = "products.html"

    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


pruducts = [
  Products("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
          "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
  Products("Panic! At The Disco",
          "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
  Products("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
          "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
  Products("Metallica",
          "https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
  Products("Bad Bunny",
          "https://www.clashmusic.com/sites/default/files/sty…e/Bad-Bunny-YHLQMDLG-Album-2020.jpg?itok=tbZNj82L", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
  Products("Kaskade",
          "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
]


class Show(TemplateView):
    template_name = "show.html"


class Login(TemplateView):
    template_name = "login.html"


class Wishlist(TemplateView):
    template_name = "wishlist.html"


class Cart(TemplateView):
    template_name = "cart.html"


class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products # this is where we add the key into our context object for the view to use
        return context



