from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # user_id = models.ForeignKey(User,ondelete=models.CASCADE)