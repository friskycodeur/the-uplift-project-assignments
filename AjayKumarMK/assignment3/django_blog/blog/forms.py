from django.forms import ModelForm
from .models import blog
from django import forms

class CreateBlog(forms.Form):
    title = forms.CharField(label='Blog Title', max_length=100)
    content = forms.CharField(label='Blog Description',widget=forms.Textarea)

class UpdateBlog(forms.Form):
    title = forms.CharField(label='Blog Title', max_length=100)
    content = forms.CharField(label='Blog Description',widget=forms.Textarea)
