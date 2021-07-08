from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name ='blog-welcome'),
    path('signup',views.signup),
    path('signin',views.signin),
    path('signout',views.signout)
]
