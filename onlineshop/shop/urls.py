from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
]