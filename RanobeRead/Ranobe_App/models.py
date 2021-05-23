from django.db import models

class User(models.Model):
    login = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Author(models.Model):
    name = models.CharField(max_length=20)

class Ranobe(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField()
    description = models.TextField()
    japaneseName = models.CharField(max_length=60)
    englishName = models.CharField(max_length=60)
    translator = models.CharField(max_length=20)
    editor = models.CharField(max_length=20)
    statusOfTranslate = models.CharField(max_length=20)
    statusOfTitle = models.CharField(max_length=20)


class Ranobe_Reading(models.Model):
    name = models.CharField(max_length=60)
    product = models.ForeignKey(Ranobe, on_delete=models.CASCADE)
    text = models.TextField()

class Applicant(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
