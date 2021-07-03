from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.email}"