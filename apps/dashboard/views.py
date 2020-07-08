from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, RegisterForm, MaterialForm, StorageForm
from apps.api.models import Member
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_authenticated:
            #login(request, user)
            return redirect('dashboard')
        else:
            form = LoginForm()
            return render(request, 'backend/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'backend/login.html', {'form':form})


def logout(request):
    return redirect('/login')


def dashboard(request):
    q = Member.objects.all()
    return render(request, 'backend/index.html')
    

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('create member successfully')
    else:
        form = RegisterForm()
        return render(request, 'backend/area.html',{'form':form})


def material(request):
    form = MaterialForm()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Create Material succesfully')
    else:
        form = MaterialForm()
        return render(request, 'backend/material.html', {'form':form})


def storage(request):
    form = StorageForm()
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added Storage successfully')

    else:
        form = StorageForm()
        return render(request, 'backend/storage.html', {'form':form})
