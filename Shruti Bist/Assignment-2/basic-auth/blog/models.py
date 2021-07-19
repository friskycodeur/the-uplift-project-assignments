from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)