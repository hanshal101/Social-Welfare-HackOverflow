from datetime import datetime
from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    details = models.CharField(max_length=100)

class Updates(models.Model):
    headline= models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class events(models.Model):
    Title= models.CharField(max_length=50)
    Date = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)

class Room(models.Model):
    name = models.CharField(max_length=10000000)


class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100000000)
    Room = models.CharField(max_length=10000000)


class Locate(models.Model):
    name = models.CharField
