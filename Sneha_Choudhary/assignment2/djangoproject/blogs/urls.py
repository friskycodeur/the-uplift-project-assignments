from django.urls import path
from blogs import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',views.home),
    path('login/', auth_views.LoginView.as_view(template_name='signin.html'),name="login"), # create
    path('signup/',views.register,name="signup"), # create
    path('login/blogworld/', views.blogs,name='blogs'), # read
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('dashboard/create',views.create_blog,name='create'), # create
    path('blogworld/create/',views.create_blog,name='create'),
    path('blogworld/create/create',views.create_blog,name='create'),
    path('dashboard/update/<int:id>',views.update_blog), # update
    path('login/blogworld/update/<int:id>',views.update_blog,name='update'),
    path('dashboard/delete/<int:id>',views.delete_blog), # delete
    path('login/blogworld/delete/<int:id>',views.delete_blog), # delete
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
   
]