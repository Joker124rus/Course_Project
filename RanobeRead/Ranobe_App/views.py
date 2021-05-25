from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    ranobes_genres = Ranobe.genres
    ranobes = Ranobe.objects.all()
    return render(request, 'index.html', {"ranobes": ranobes, "ranobes_genres": ranobes_genres, "num_visits": num_visits})

def aboutUs(request):
    return render(request, 'aboutUs.html')

def vacancy(request):
    return render(request, 'vacancy.html')

def profile(request):
    return render(request, 'user.html')

def ranobe(request):

    return render(request, 'ranobe.html')

def ranobe_page(request, id):
    ranobe = Ranobe.objects.get(id = id)

    chaptersList = []
    ranobes = Ranobe_Reading.objects.all()
    for r in ranobes:
        if r.ranobe.id == id:
            chaptersList.append(r)
    min = -1
    for r in chaptersList:
        if r.id < -1 or min == -1 and r.ranobe.id == id:
            min = r.id
    chapterId = min

    #request.session["ranobe_id"] = id
    return render(request, 'ranobe_page.html', {"ranobe" : ranobe, "chapterId": chapterId})

def reader(request, id, chapterId):
    #ranobe_id = request.session["ranobe_id"]
    ranobe_read = Ranobe_Reading.objects.get(ranobe_id = id, id = chapterId)
    chaptersList = []
    ranobes = Ranobe_Reading.objects.all()
    for r in ranobes:
        if r.ranobe.id == id:
            chaptersList.append(r)
    now = 0
    prev = 0
    prevChapterId = 0
    next = 0
    nextChapterId = 0
    for i in range(len(chaptersList)):
        if chaptersList[i].id == chapterId:
            now = i
    if now == 0:
        prev = None
    else:
        prev = now - 1
    if now == len(chaptersList) - 1:
        next = None
    else:
        next = now + 1
    if prev is not None:
        prevChapterId = chaptersList[prev]
    else:
        prevChapterId = None
    if next is not None:
        nextChapterId = chaptersList[next]
    else:
        nextChapterId = None


    return render(request, 'ranobe_reader.html', {"chaptersList": chaptersList, "ranobe_read": ranobe_read,
                                                  "prev": prevChapterId, "next": nextChapterId})

@csrf_exempt
def login_(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    username = request.POST.get('login', None)
    password = request.POST.get('password', None)
    if username is None or password is None:
        return render(request, 'index.html', locals())
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = "Error of user authentication"
                return render(request, 'index.html', locals())
        else:
            error = "User is incorrect"
            return render(request, 'index.html', locals())

@csrf_exempt
def registration(request):
    if request.method == "POST":
        username = request.POST.get('login', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password_repeat = request.POST.get('password_repeat', None)
        if password != password_repeat:
            return render(request, 'registration.html', locals())
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


@csrf_exempt
def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')



