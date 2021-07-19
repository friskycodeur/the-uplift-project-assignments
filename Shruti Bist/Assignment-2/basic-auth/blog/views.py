from django.shortcuts import render, redirect
from . models import blog
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url='/auth/login')
def blogs(request):
    print("here")
    print("this is current logged in user",request.user.email)
    # blogs = blog.objects.all()
    blogs = blog.objects.filter(user_id=request.user)
    return render(request,'blogs.html',{'blogs':blogs})


def create_blog(request):
    if request.method == 'GET':
        return render(request,'create.html')
    else:
        #### get the form data from user
        print(request.POST)
        blog.objects.create(title=request.POST["title"],description=request.POST["description"],user_id=request.user)
        return redirect('blogs')


def update_blog(request,id):
    if request.method == 'GET':
        blogs = blog.objects.get(id=id)
        return render(request,'edit.html',{'blogs':blogs})
    else:
        blog.objects.filter(id=id).update(title=request.POST["title"],description=request.POST["description"])
        # blogs = blog.objects.all()
        return redirect('blogs')

        # return render(request,'blogs.html',{'blogs':blogs})



def delete_blog(request,id):
    blog.objects.filter(id=id).delete()
    return redirect('blogs')