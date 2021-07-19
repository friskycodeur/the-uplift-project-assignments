from django.urls import path
from . import views
from django.conf.urls import url, include


urlpatterns = [
    path('', views.blogs,name='blogs'), # read
    path('create',views.create_blog), # create
    path('update/<int:id>',views.update_blog), # update
    path('delete/<int:id>',views.delete_blog) # delete
]