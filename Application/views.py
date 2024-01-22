# Application/views.py
from django.shortcuts import render
from .models import *

def Application(request):
    return render(request, 'index.html')
