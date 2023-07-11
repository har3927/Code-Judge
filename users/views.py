from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import  CreateUserForm
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('judge/index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request , 'Logged in successfully..')
                return render(request,'judge/index.html',{})
            else:
                messages.info(request , 'The username or password is incorrect..')
                return redirect('/auth/login_user')
        else:
            return render(request, 'auth/login.html' , {})

def register_user(request):
    if request.user.is_authenticated:
        return render(request,'judge/index.html',{})
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Your account is created, you can now login as ' + user)
                return redirect('/auth/login_user')


        context = { 'form' : form }
        return render(request, 'auth/register.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out..')
    return render(request,'judge/index.html',{})
