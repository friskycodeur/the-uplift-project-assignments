from django.shortcuts import render, redirect
from . models import blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authLogin
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        # login LOGIC
        username,_ =  request.POST["email"].split("@")
        user = authenticate(request,username=username,password=request.POST["password"])
        if user is not None:
            authLogin(request,user)
            context={"messages":f"Welcome {user} sign in successful"}
            print("sign in sucees")
            # return render(request,'signin.html',context=context)
            return redirect('blogs')
            
        else:
            context={"messages":"invalid credentials"}
            return render(request,'signin.html',context=context)


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        """ signup logic """
        username,_ =  request.POST["email"].split("@")
        is_exist = User.objects.filter(username = username).exists()
        if is_exist:
            print("user already exist")
            context={"messages":"User already exist.You may login"}

            return render(request,'signup.html',context=context)
        else:
            myuser = User.objects.create_user(username=username,email = request.POST["email"],password=request.POST["password"])
            print("myuser",myuser)
            context={"messages":f"Welcome sign up successfull {myuser}"}

            return render(request,'signup.html',context=context)

def blogs(request):
    if request.user.is_authenticated:
        print(request.user.username)
    blogs=blog.objects.filter(curruser=request.user.username) 
    context={"blogs" : blogs} 
    for object in blogs:     
        print(object.title)    
    return render(request,"blog.html",{'blogs':blogs})   

def dashboard(request):
    return render(request,"blog.html")    

def home(request):
    return render(request,'homepage.html')

def create_blog(request):
    if request.method == 'GET':
        username=request.user.username
        return render(request,'create.html',{'username':username})
    else:
        #### get the form data from user
        print(request.POST)
        blog.objects.create(curruser=request.user.username,title=request.POST["title"],description=request.POST["description"])
        return redirect('blogs')

def update_blog(request,id):
    if request.method == 'GET':
        username=request.user.username
        blogs = blog.objects.get(id=id)
        return render(request,'update.html',{'username':username,'blogs':blogs})
    else:
        blog.objects.filter(id=id).update(title=request.POST["title"],description=request.POST["description"])
        # blogs = blog.objects.all()
        return redirect('blogs')

        # return render(request,'blogs.html',{'blogs':blogs})



def delete_blog(request,id):
    blog.objects.filter(id=id).delete()
    return redirect('blogs')