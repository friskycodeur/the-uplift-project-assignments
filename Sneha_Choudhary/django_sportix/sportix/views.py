from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authLogin
from .forms import NameForm,UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import match,Room,Message
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Create your views here.
def home(request):
    if request.method == "POST":
        print("Hello2")
        form =NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            messages.add_message(request,messages.INFO,form.cleaned_data.get('name'))
            context={"name":name}
            print("Hello2")
            return HttpResponseRedirect("membership")
        else :
           context={"messages":f"Not Valid "}
           return render(request,'index.html',context=context)
    else:
        form=NameForm()
        print("Hello3")   
        return render(request,"index.html",{'form':form})


def membership(request):
    storage=get_messages(request)
    name=None
    for message in storage:
        name=message
        break
    
    if request.method == "POST":
        print("Helljko2")
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Hellllo2")
            return redirect("login")
        else :
           context={"messages":f"Not Valid "}
           return render(request,'password.html',context=context)
    else:
        form=UserRegisterForm()
        print("Hehiujllo3 ") 
        return render(request,"password.html",{'form':form,'name':name})   

def sports(request):
    if request.method == "POST":
        print("Hello")
        search=  request.POST["search"]
        matches=match.objects.filter(name__contains=search)
        for object in matches:
          print(object.name)
        return render(request,"search.html",{'user':request.user.username,'search':search,'matches':matches})
    else:    
       ipl_matches=match.objects.filter(category="IPL")
       mw_matches=match.objects.filter(status="MW") 
       ra_matches=match.objects.filter(status="RA") 
       tr_matches=match.objects.filter(status="TR") 
       olympics_matches=match.objects.filter(category="OLYMPICS")
       return render(request,"sports.html",{'user':request.user.username,'ipl_matches':ipl_matches,'tr_matches':tr_matches,'mw_matches':mw_matches,'ra_matches':ra_matches,'olympics_matches':olympics_matches})        

def play(request,id):
    matches=match.objects.filter(id=id).order_by('date')
    for object in matches:
        room=Room.objects.filter(name=object.name)
    return render(request,"play.html",{'matches':matches,'room':room})

def send(request,id):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=request.user.username, room=id)
    new_message.save()
    print("message")
    return HttpResponse('Message sent successfully')

def getMessages(request, id):
    room_details = Room.objects.get(id=id)

    messages = Message.objects.filter(room=id)
    for object in messages:
       print(object.value)
    return JsonResponse({"messages":list(messages.values())})

def more(request,id):
    if id==1:
        more_of="ipl"
        matches=match.objects.filter(category="IPL").order_by('date')
    if id==2:
        more_of="olympics"
        matches=match.objects.filter(category="OLYMPICS").order_by('date')
    if id==3:
        more_of="recently added"
        matches=match.objects.filter(status="RA").order_by('date')
    if id==4:
        more_of="most watched"           
        matches=match.objects.filter(status="MW").order_by('date') 
    return render(request,"more.html",{'matches':matches,'moreof':more_of})    