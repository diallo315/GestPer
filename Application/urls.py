# Application/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', loginsignup, name='loginsignup'),
    path('dashboard', dashboard, name='dashboard'),
    path('personnel', personnel, name='personnel'),
    path('document', doucument, name='document'),
    path('formationcours', formationcours, name='formationcours'),
    path('historique', historique, name='historique'),
    path('inscritformation', inscritformation, name='inscritformation'),
    path('conge', conge, name='conge'), 
    path('sanction', sanction, name='sanction'),
]
