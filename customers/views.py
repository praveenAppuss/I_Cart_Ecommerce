from email.headerregistry import Address
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Customer
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
    
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            # creates user accounts
            user= User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # create customer account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_message="user registred successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="username invalid"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            # error_message="username or password invalid"
            messages.error(request,"invlid login")
            
    return render(request,'account.html',context)

def logouts(request):
    auth.logout(request)
    return redirect('/')