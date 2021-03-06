"""RanobeRead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Ranobe_App import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name="index_url"),
        path('login', views.login_, name="login_url"),
        path('logout', views.logout_, name="logout_url"),
        path('ranobe/<int:id>/<int:chapterId>/', views.reader, name="reader_url"),
        path("ranobe/<int:id>", views.ranobe_page, name = "ranobe_page_url"),
        path('ranobe/', views.ranobe, name="ranobe_url"),
        path('registration/', views.registration, name="registration_url"),
        path('aboutUs/', views.aboutUs, name="aboutUs_url"),
        path('profile/', views.profile, name="profile_url"),
        path('vacancy/', views.vacancy, name="vacancy_url")
]
