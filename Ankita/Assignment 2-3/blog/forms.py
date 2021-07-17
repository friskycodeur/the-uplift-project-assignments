from django import forms

class CreateBlog(forms.Form):
    title=forms.CharField(label='Blog_title',max_length=100)
    description=forms.CharField(label='Blog_description',max_length=100)