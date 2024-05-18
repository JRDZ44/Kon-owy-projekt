from django.db import models


# tworzy model uzytkownika
class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)


# tworzy model kategorii dla pracownika
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)


# tworzy model posiadający informacje o firmie
class AboutUs(models.Model):
    info = models.TextField(max_length=500)


# tworzy model produktów
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# tworzy model udzielający informacji o kontakcie
class ContactUs(models.Model):
    text = models.TextField(max_length=100)


# tworzy model informujący o sponsorach
class Sponsors(models.Model):
    text = models.TextField(max_length=200)


# tworzy model informujący o wymaganiach w firmie
class Requirements(models.Model):
    text = models.ManyToManyField(Users)

# Create your models here.
