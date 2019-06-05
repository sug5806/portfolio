from django.urls import path
from .views import *

app_name = 'dabang'

urlpatterns = [
    path('', Dabang_List.as_view(), name='list'),
    # path('search/', Dabang_search.as_view(), name='search'),
    path('search/', dabang_Search, name='search'),
]