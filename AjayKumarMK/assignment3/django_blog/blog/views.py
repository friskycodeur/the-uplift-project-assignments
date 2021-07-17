from django.shortcuts import render,redirect
from . models import blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CreateBlog,UpdateBlog
# Create your views here.

@login_required(login_url='/')
def home(request):
    blogs = blog.objects.all()
    username = request.user
    return render(request,'blog/blog.html',{'blogs' : blogs,'username':username})

@login_required(login_url='/')
def create(request):
    if request.method == 'GET':
            form = CreateBlog()
            username = request.user
            return render(request,'blog/create.html',{'form':form,'username':username})
    else:
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.cleaned_data["author"] = request.user
            blog.objects.create(**form.cleaned_data)
            
        
        return redirect('/blogs/')

@login_required(login_url='/')
def update(request, id):
    if request.method == 'GET':
        post = blog.objects.get(id=id)
        username = request.user
        data = {
            'title' : post.title,
            'content' : post.content
        }
        form = UpdateBlog(data)
        return render(request,'blog/update.html',{'form':form,'username':username,'post':post})
    else:
        blog.objects.filter(id=id).update(title=request.POST["title"],content=request.POST["content"])
        return redirect('/blogs/')

def posts(request,id):
    posts = blog.objects.get(id=id)
    username = request.user
    if username == posts.author:
        context = "yes"
        return render(request,'blog/posts.html', {'posts': posts, 'context':context,'username':username})
    return  render(request,'blog/posts.html', {'posts': posts,'username':username})



def signout(request):
    logout(request)
    print("Logged out succesful")
    return redirect('/')

@login_required(login_url='/')
def delete(request,id):
     if request.method == 'GET':
        posts = blog.objects.get(id=id)
        username = request.user
        if username == posts.author:
            blog.objects.filter(id=id).delete()
            return redirect('/blogs/')
        return redirect('/blogs/')