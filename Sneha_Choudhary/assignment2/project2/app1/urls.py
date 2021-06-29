from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home),
    path('login/',views.login,name="login"), # create
    path('signup/',views.signup,name="signup"), # create
    path('blogworld/', views.blogs,name='blogs'), # read
    path('create',views.create_blog), # create
    path('update/<int:id>',views.update_blog), # update
    path('delete/<int:id>',views.delete_blog) # delete
   
]