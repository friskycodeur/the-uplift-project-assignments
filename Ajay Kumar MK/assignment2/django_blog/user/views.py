from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        username = request.POST['username']
        is_exist = User.objects.filter(username = username).exists()
        if is_exist:
            print("User Already Exists")
            context = {'messages' : "Username already exists!"}
            return render(request,'signup.html',context)
        else:
            myuser = User.objects.create_user(email=request.POST['email'],username=request.POST['username'],password=request.POST['password'])
            print("myuser",myuser)
            context = {'messages':f"Welcome, signup successful {myuser}"}
            return render(request,'signin.html',context)


def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("User:",username)
            return redirect('blogs/')
        else:
            context = {"messages":"Invalid Credentials"}
            print(context)
            return render(request,"signin.html",context=context)

def signout(request):
    logout(request)
    print("Logged out succesful")
    return redirect('/')