from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name ='blog-home'),
    path('create/',views.create, name = 'blog-create'),
    path('post/<int:id>',views.post),
    path('post/update/<int:id>/',views.update),
    path('post/delete/<int:id>',views.delete)
]
