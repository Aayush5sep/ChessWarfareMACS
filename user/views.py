from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserDetails

# Create your views here.

def loginpage(request):
    return render(request,'user/login.html')

def signuppage(request):
    return render(request,'user/signup.html')


    
def loginuser(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")

def temp(request):
    return render(request,'user/signup profile.html')

def profileupdate(request):
    user = request.user
    phone = request.POST['phone']
    age = request.POST['age']
    about = request.POST['about']
    is_student = request.POST.get('is_student')
    student = False
    if is_student is not None:
        student=True
    profiled = UserDetails.objects.get(user=user)
    profiled.phone = phone
    profiled.age = age
    profiled.about = about
    profiled.student = student
    profiled.save()
    messages.success(request,'Profile Updated')
    return redirect("/")
