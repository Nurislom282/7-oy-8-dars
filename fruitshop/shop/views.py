from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductView(ListView):
    model = Product