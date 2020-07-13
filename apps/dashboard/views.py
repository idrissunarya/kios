from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, RegisterForm, MaterialForm, StorageForm
from apps.api.models import Member, Storage, Material
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework import viewsets
from apps.api.serializers import MaterialSerializer, MemberSerializer
from rest_framework import generics

class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all().order_by('id')
    serializer_class = MaterialSerializer

class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all().order_by('username')
    serializer_class = MemberSerializer



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User is valid, active and authenticated")
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'User and Password invalid !')
            form = LoginForm()
            return render(request, 'backend/login-prod.html', {'form':form})    
    else:
        form = LoginForm()
        return render(request, 'backend/login-prod.html', {'form':form})
        

def dashboard(request):
    queryset = User.objects.all()
    context = {'queryset':queryset}
    return render(request, 'backend/index.html', context)


def logout(request):
    user = None
    request.session.flush()
    return redirect('login')
    

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
            return redirect('storage_list')
    else:
        form = StorageForm()
        return render(request, 'backend/storage.html', {'form':form})

def storage_list(request):
    queryset = Storage.objects.all()
    context = {'queryset':queryset}
    return render(request, 'backend/successed/storage_success.html', context)

