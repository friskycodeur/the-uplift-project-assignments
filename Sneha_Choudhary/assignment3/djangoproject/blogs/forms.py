from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import blog


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'username','email', 'password1','password2']

class CreateBlog(forms.Form):
    title = forms.CharField(label='Blog Title', max_length=100)
    description = forms.CharField(label='Blog Description', widget=forms.Textarea)

class UpdateBlog(forms.Form):
    title = forms.CharField(label='Blog Title', max_length=100)
    description = forms.CharField(label='Blog Description',widget=forms.Textarea)    