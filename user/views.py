from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from .models import UserDetails
from dotenv import load_dotenv
import os
load_dotenv()

# Create your views here.

def loginpage(request):
    return render(request,'user/login.html')

def signuppage(request):
    return render(request,'user/signup.html')

def signupuser(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone = request.POST['phone']
        authcode = request.POST['authcode']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)


        rkey = os.environ['REGISTRATION_KEY']
        skey = os.environ['SETUP_KEY']
        akey = os.environ['ARBITER_KEY']

        is_register_staff = False
        is_duel_staff = False
        is_arbiter = False
        if authcode == rkey:
            is_register_staff = True
            reg_grp = Group.objects.get(name='Registration Staff')
            reg_grp.user_set.add(newuser)
            newuser.is_staff = True
            newuser.save()
        elif authcode == skey:
            is_duel_staff = True
            setup_grp = Group.objects.get(name='Manage Duel Staff')
            setup_grp.user_set.add(newuser)
        elif authcode == akey:
            is_arbiter = True
            arbiter_grp = Group.objects.get(name='Arbiters')
            arbiter_grp.user_set.add(newuser)
        
        userd=UserDetails(user=user,fname=fname,lname=lname,phone=phone,
                          is_register_staff=is_register_staff,is_duel_staff=is_duel_staff,is_arbiter=is_arbiter)
        userd.save()
        messages.success(request,"User Account Created Successfully")
        return redirect('/')
    else:
        return HttpResponse("Creating new user account failed !")
    
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
