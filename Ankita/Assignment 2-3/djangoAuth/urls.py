from django.urls import path
from . import views
from django.conf.urls import url, include


urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
]