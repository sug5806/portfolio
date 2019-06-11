from django.contrib import admin
from .models import Category, Product
# from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



# class CategoryAdmin(SummernoteModelAdmin):
#     summernote_fields = ['description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created',
                    'updated']
    list_filter = ['available_display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']

# class ProductAdmin(SummernoteModelAdmin):
#     summernote_fields = ['description', ]

admin.site.register(Product, ProductAdmin)
