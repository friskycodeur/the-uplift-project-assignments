from django.db import models


# Create your models here.


class blog(models.Model):
    curruser=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description = models.TextField()         
