from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import *

class ProductList(ListView):
    model = Product
    template_name = 'shop/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Category.objects.filter(parent_category=Category.objects.get(pk=2)).order_by('name')
        kwargs.update({'categories': categories})
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        # print(queryset)

        if 'slug' in self.kwargs:
            category = Category.objects.filter(slug=self.kwargs['slug'])
            # print(category[0])
            if category.exists():
                category |= self.get_category_list(category[0])
                queryset = queryset.filter(category__in=category)
            else:
                queryset = queryset.none()
        return queryset

    def get_category_list(self, category):
        categories = category.sub_categories.all()
        for category in categories:
            categories |= self.get_category_list(category)
        print("categories : ", categories)
        return categories


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'