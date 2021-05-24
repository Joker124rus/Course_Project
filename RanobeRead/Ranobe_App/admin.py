from django.contrib import admin
from .models import User, Genre, Author, Ranobe, Ranobe_Reading, Applicant

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Ranobe)
admin.site.register(Ranobe_Reading)
admin.site.register(Applicant)
