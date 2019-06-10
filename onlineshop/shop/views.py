from django.shortcuts import render
from .models import Category, Product

from django.views.generic import ListView, DetailView, DeleteView, CreateView

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'shop/product_list.html'