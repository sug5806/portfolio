from django.urls import path
from .views import *

app_name = 'comment'

urlpatterns = [
    path('add_comment/', add_comment, name='add_comment'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
]