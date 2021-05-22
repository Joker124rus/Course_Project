from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ranobe(request):
    return render(request, 'ranobe.html')