from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    ranobes = Ranobe.objects.all()
    return render(request, 'index.html', {"ranobes": ranobes, "num_visits": num_visits})

def ranobe(request):
    return render(request, 'ranobe.html')

def ranobe_page(request, id):
    ranobe = Ranobe.objects.get(id = id)
    return render(request, 'ranobe_page.html', {"ranobe" : ranobe})

#def registration(request):
#    return render(request, 'registration.html')

@csrf_exempt
def login_(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username is None or password is None:
        return render(request, 'example_app/login.html', locals())
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = "Error of user authentication"
                return render(request, 'example_app/login.html', locals())
        else:
            error = "User is incorrect"
            return render(request, 'example_app/login.html', locals())

@csrf_exempt
def registration(request):
    if request.method == "POST":
        username = request.POST.get('login', None)
        password = request.POST.get('password', None)
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Такой пользователь уже существует")
            else:
                user = User.objects.create_user(username=username, password=password)
        except:
            pass
        if username is None or password is None:
            return render(request, 'registration.html', locals())
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
    return render(request, 'registration.html', locals())



