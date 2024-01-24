# Application/views.py
from django.shortcuts import render
from .models import *
# views.py
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import io
import base64

def my_chart_view(request):
    # Exemple de données (à remplacer par vos données réelles)
    labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5']
    values = [10, 10, 10, 20, 50]

    # Créer un graphique
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('My Pie Chart')

    # Convertir le graphique en image
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Renvoyer l'image générée dans la réponse HTTP
    response = HttpResponse(image_stream.getvalue(), content_type='image/png')
    return response








def dashboard(request):
    # Exemple de données (à remplacer par vos données réelles)
    labels = ['Label 1', 'Label 2', 'Label 3']
    values = [30, 40, 30]

    # Personnaliser le graphique circulaire
    colors = ['gold', 'lightcoral', 'lightskyblue']

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('My Customized Pie Chart')

    # Convertir le graphique en image
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Convertir l'image en base64
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    return render(request, 'src/dashboard.html', {'image': image_base64})
def loginsignup(request):
    return render(request, 'loginSignup.html')

def personnel(request):
    return render(request, 'src/personnel.html')

def doucument(request):
    return render(request, 'src/document.html')

def conge(request):
    return render(request, 'src/conge.html')

def sanction(request):
    return render(request, 'src/sanction.html')

def inscritformation(request):
    return render(request, 'src/inscritformation.html')

def historique(request):
    return render(request, 'src/historique.html')

def formationcours(request):
    return render(request, 'src/formationcours.html')



