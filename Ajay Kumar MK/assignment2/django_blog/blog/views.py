from django.shortcuts import render,redirect
from . models import blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signin')
def home(request):
    blogs = blog.objects.filter(user_id=request.user.id)
    return render(request,'blog.html', {'blogs': blogs})

@login_required(login_url='/signin')
def create(request):
    if request.method == 'GET':
        return render(request,'create_blog.html')
    else:
        blog.objects.create(title=request.POST["title"],content=request.POST["content"],user_id = request.user)
        return redirect('/blogs/')

@login_required(login_url='/signin')
def post(request, id):
    blogs = blog.objects.get(id=id)
    return render(request,'posts.html', {'blogs': blogs})

@login_required(login_url='/signin')
def update(request, id):
    if request.method == 'GET':
        blogs = blog.objects.get(id=id)
        return render(request,'edit.html',{'blogs': blogs})
    else:
        blog.objects.filter(id=id).update(title=request.POST["title"],content=request.POST["content"])
        return redirect('/blogs/')

def delete(request,id):
    blog.objects.filter(id=id).delete()
    return redirect('/blogs/')