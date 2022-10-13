from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_products = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Size(models.Model):

    title = models.CharField(max_length=500)
    title = models.CharField(max_length=150)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="sizes")

    def __str__(self):
        return self.title


# Wishlist model
class Wishlist(models.Model):

    title = models.CharField(max_length=150)
    # this is many-to-many field, this will create our join table
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.title