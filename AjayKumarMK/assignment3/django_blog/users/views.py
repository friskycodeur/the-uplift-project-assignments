from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request,'users/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            context = {'messages' : "User Created Successfully."}
            return render(request,'users/register.html',context)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def signin(request):
    if request.method == 'GET':
        return render(request,'users/signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("User:",username)
            return redirect('/blogs/')
        else:
            context = "Invalid Credentials"
            print(context)
            return render(request,"users/signin.html",{'context':context})