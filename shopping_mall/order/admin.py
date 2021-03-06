from django.contrib import admin

from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product', ]

class OrderOption(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'paid', 'created', 'updated', ]
    list_editable = ['paid']
    inlines = [OrderItemInline]
admin.site.register(Order, OrderOption)