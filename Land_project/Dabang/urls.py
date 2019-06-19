from django.urls import path
from .views import *

app_name = 'dabang'

urlpatterns = [
    path('', Dabang_List.as_view(), name='list'),
    path('search/', dabang_Search, name='search'),
    # path('tf/', TF, name='TF'),
]