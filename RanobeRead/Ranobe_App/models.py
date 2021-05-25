from django.db import models

"""class User(models.Model):
    login = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.login"""

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ranobe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    date = models.DateField()
    image = models.CharField(max_length=300)
    description = models.TextField()
    japaneseName = models.CharField(max_length=200)
    englishName = models.CharField(max_length=200)
    translator = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    statusOfTranslate = models.CharField(max_length=50)
    statusOfTitle = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ranobe_Reading(models.Model):
    name = models.CharField(max_length=150)
    chapterNumber = models.IntegerField()
    ranobe = models.ForeignKey(Ranobe, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return (f"{self.chapterNumber} - {self.name}")

class Applicant(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name
