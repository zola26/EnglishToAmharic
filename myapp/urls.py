# myapp/urls.py

from django.urls import path
from .views import index, convert

urlpatterns = [
    path('', index, name='index'),
    path('convert/', convert, name='convert'),
]
