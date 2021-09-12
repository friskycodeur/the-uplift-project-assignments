from django.contrib import admin
from .models import match,Room,Message
from django.db import models

# Register your models here.


admin.site.register(Room)
admin.site.register(Message)
admin.site.register(match)