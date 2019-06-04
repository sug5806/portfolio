from django.urls import path
from .views import *


urlpatterns = [
    path('', Dabang_List.as_view(), name='list'),
]