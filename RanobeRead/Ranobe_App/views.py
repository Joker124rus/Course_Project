from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    ranobes = Ranobe.objects.all()
    return render(request, 'index.html', {"ranobes": ranobes})

def ranobe(request):
    return render(request, 'ranobe.html')

def ranobe_page(request, id):
    ranobe = Ranobe.objects.get(id = id)
    return render(request, 'ranobe_page.html', {"ranobe" : ranobe})

def registration(request):
    return render(request, 'registration.html')