from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password,check_password
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
        userData.password = make_password(object.password)
        userData.signup()
        if userData.exists():
            print("user successfully logged in ")
            print("userdata",userData[0])
            context={"messages":f"welcome {userData[0].email}"}
            return render(request,'welcome.html',context=context)
        else:
            print("invalid credentials")
            context={"messages":"invalid credentials"}
            return render(request,'signin.html',context)


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        """
            IT means request.method is POST
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
                print("ok password length is greator than 6")
                """
                    insert into User values(request.POST["email"],request.POST["password"])
                """
                User.objects.create(email = request.POST["email"],password=request.POST["password"])
                object.password = make_password(object.password)
                object.signup()
                print("user successfully created")
                context={"messages":"user successfully created"}
                return render(request,'signup.html',context)
            else:
                print("password is not ok")
                context={"messages":"password length is short"}
                return render(request,'signup.html',{"messages":"password length is short"})
        