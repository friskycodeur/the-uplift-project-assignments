from django.shortcuts import render, redirect
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
            context={"messages":f"Welcome sign in successfull {user}"}

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
            context={"messages":"user already exist"}

            return render(request,'signin.html',context=context)
        else:
            myuser = User.objects.create_user(username=username,email = request.POST["email"],password=request.POST["password"])
            print("myuser",myuser)
            context={"messages":f"Welcome sign up successfull {myuser}"}

            return render(request,'signin.html',context=context)