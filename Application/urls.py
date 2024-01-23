# Application/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', template, name='template'),
    path('dashboard', dashboard, name='dashboard'),
]
