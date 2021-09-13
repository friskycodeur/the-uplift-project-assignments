from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

STATUS_CHOICES=[
    ('MW','MOST WATCHED'),
    ('RA','RECENTLY ADDED'),
    ('TR','TOP RATED')
]
# Create your models here.
class match(models.Model):
    name=models.CharField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.CharField(max_length=100)
    sport=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='')
    status=models.CharField(choices=STATUS_CHOICES, max_length=2)
    video = models.FileField(upload_to='')
    link=models.CharField(max_length=300)

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000,null=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    user = models.CharField(max_length=1000000,null=True)
    room = models.CharField(max_length=1000000,null=True)

