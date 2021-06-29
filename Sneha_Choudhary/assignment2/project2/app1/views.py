from django.shortcuts import render, redirect
from . models import blog
from .models import User
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        print(request.POST)
        """
            LOGIN LOGIC
                1. email exists or not
                2. password is correct or not
        """
        userData = User.objects.filter(email = request.POST["email"],password=request.POST["password"])
        if userData.exists():
            print("user successfully logged in ")
            print("userdata",userData[0])
            context={"messages":f"welcome {userData[0].email}"}

            return redirect("blogs")
        else:
            print("invalid credentials")
            context={"messages":"invalid credentials"}
            return render(request,'signin.html',context)


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        """
            MAIN SIGNUP LOGIC
        """
        print(request.POST)
        """
            select * from user where email = request.POST["email"];
        """
        if User.objects.filter(email = request.POST["email"]).exists():
            context={"messages":"This email is already registered"}
            return render(request,'signup.html',{"context":context})
        else:
            if len(request.POST["password"]) > 6:
                print("ok password length is greator then 6")
                """
                    insert into User values(request.POST["email"],request.POST["password"])
                """
                User.objects.create(email = request.POST["email"],password=request.POST["password"])
                print("user successfully created")
                context={"messages":"user successfully created"}

                return render(request,'signup.html',context)

            else:
                print("password is not ok")
                context={"messages":"password length is short"}
                return render(request,'signup.html',{"messages":"password length is short"})

def blogs(request):
    if request.user.is_authenticated():
        blogs=blog.objects.filter(user=request.user)
    return render(request,'blog.html',{'blogs':blogs})

def home(request):
    return render(request,'homepage.html')

def create_blog(request):
    if request.method == 'GET':
        return render(request,'create.html')
    else:
        #### get the form data from user
        print(request.POST)
        blog.objects.create(title=request.POST["title"],description=request.POST["description"])
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