from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class artist(models.Model):
    name = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    moviename = models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
