from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home),
    path('login/',views.login,name="login"), # create
    path('signup/',views.signup,name="signup"), # create
    path('blogworld/', views.blogs,name='blogs'), # read
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/create',views.create_blog,name='create'), # create
    path('blogworld/create/',views.create_blog,name='create'),
    path('blogworld/create/create',views.create_blog,name='create'),
    path('dashboard/update/<int:id>',views.update_blog), # update
    path('blogworld/update/<int:id>',views.update_blog,name='update'),
    path('dashboard/delete/<int:id>',views.delete_blog), # delete
    path('blogworld/delete/<int:id>',views.delete_blog) # delete
   
]