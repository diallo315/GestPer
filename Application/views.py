# Application/views.py
from django.shortcuts import render
from .models import *

def template(request):
    return render(request, 'template.html')
def dashboard(request):
    return render(request, 'src/dashboard.html')
