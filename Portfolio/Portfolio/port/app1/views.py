from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.models import User
from app1.models import Contact
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'index.html')
def resume(request):
    return render(request,'resume.html')
def experience(request):
    return render(request,'experience.html')

def home(request):
    return render(request,"home.html")

# contact function---------------------
def ContactP(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        city=request.POST.get("city")
        purpose=request.POST.get("purpose")
        r=Contact(name=name,email=email,mobile=mobile,city=city,purpose=purpose)
        r.save()
        return render(request,"index.html",{'msg':'Thankyou For COnnect With Me !'})

# login form-----------------------

def login1(request):
    return render(request,"login.html")
def loginform(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    User=authenticate(username=username,password=password)

    if User is not None:
        login(request,User)
        return redirect('/home')
    else:
        return redirect('/login')
        
 # all record function----------------------

def all(request):
        
     r=Contact.objects.all
     return render(request,"all.html",{'data':r})

# delete record-----------------------

def delete(request):
    return render(request,'delete.html')
def erase(request):
    if request.method=="POST":
        name=request.POST.get('name')
        r=Contact.objects.filter(name=name)
        r.delete()
        return render(request,'delete.html',{'msg':'Successfully Deleted Recored'})
    
# update record----------------------
def update(request):
    return render(request,'update.html')
def userupdate(request):
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         city=request.POST.get('city')
         Contact.objects.filter(name=name,email=email,city=city)
         return render(request,'update.html',{'msg':'Successfully Updated'})
    

# logout-----------------

def userlogout(request):
    logout (request)
    return redirect('/index')