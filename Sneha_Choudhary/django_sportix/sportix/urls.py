from django.urls import path
from sportix import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from django_email_verification import urls as mail_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home),
    path('login/', auth_views.LoginView.as_view(template_name='signin.html'),name="login"),
    path('register/',views.membership,name="register"),
    path('sports/',views.sports,name="sports"),
    path('membership/',views.membership,name="membership"),
    path('more/<int:id>',views.more,name="more"),
    path('more/play/<int:id>',views.play,name="play"),
    #path('sports/play',views.new),
    path('sports/<int:id>',views.play,name="play"), 
    path('send/<int:id>', views.send, name='send'),
    path('getMessages/<int:id>', views.getMessages, name='getMessages'),
]    +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
