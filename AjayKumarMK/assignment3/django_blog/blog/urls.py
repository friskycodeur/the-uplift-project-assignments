from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='blog-create'),
    path('posts/<int:id>',views.posts,name='posts'),
    path('posts/update/<int:id>/',views.update,name='blog-update'),
    path('logout/',views.signout,name='logout'),
    path('posts/delete/<int:id>',views.delete)
]