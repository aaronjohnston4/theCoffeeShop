from django.contrib import admin
from .models import Products, Size # import the Artist model from models.py
# Register your models here.

admin.site.register(Products) # this line will add the model to the admin panel
admin.site.register(Size)