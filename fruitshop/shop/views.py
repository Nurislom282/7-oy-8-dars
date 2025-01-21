from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Ctegory,Subcategory
from random import randint
# Create your views here.

class ProductView(ListView):
    # model = Product
    # queryset = Product.objects.all().order_by('-created_at')
    extra_context = {
        "title":"Main Page"
    }
    template_name = "shop/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        products_list = []
        products = Product.objects.all()
        count_product = len(products)
        for i in range(8):
            index = randint(0, count_product-1)
            product = products[index]
            products_list.append(product)
        return products_list
    def get_context_data(self, object_list = None ,**kwargs):
        context = super().get_context_data()
        context["categories"] = Ctegory.objects.all()
        return context

class CardView(ListView):
    model = Product
    template_name = "shop/card.html"
    context_object_name = "products"

    def get_context_data(self, object_list = None ,**kwargs):
        context = super().get_context_data()
        context["categories"] = Ctegory.objects.all()
        return context

class shop(ListView):
    model = Product
    template_name = "shop/shop.html"
    context_object_name = "products"

    def get_context_data(self, object_list = None ,**kwargs):
        context = super().get_context_data()
        context["categories"] = Ctegory.objects.all()
        return context
