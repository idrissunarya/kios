from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, MaterialForm, StorageForm
from apps.api.models import Member, Storage, Material
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework import viewsets
from apps.api.serializers import MaterialSerializer, MemberSerializer, StorageSerializer
from rest_framework import generics

from django.core import serializers

from django_tables2 import SingleTableView


# Serializer packages
class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all().order_by('-created')
    serializer_class = MaterialSerializer

class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all().order_by('-created')
    serializer_class = MemberSerializer

class StorageListView(generics.ListAPIView):
    queryset = Storage.objects.all().order_by('-created')
    serializer_class = StorageSerializer

def api_material(request, id):
    q = Material.objects.filter(id=id)
    serialized = serializers.serialize('json', q)
    return JsonResponse(serialized, safe=False)

def delete_material(request,id):
    q = Material.objects.filter(id=id)
    q.delete()
    return JsonResponse({'status': 'success delete'}, safe=False)
    #return HttpResponseRedirect('material_add')



# Tables Django_tables2
#class TableView(tables.MaterialTableView):
#    table_class = MaterialTable
#    queryset = Material.objects.all()
#    template_name = 'backend/pages/add_material.html'


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


# Material component 
def material_add(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_add')
    else:
        queryset = Material.objects.all()
        form = MaterialForm()
        context = {'queryset':queryset, 'form':form}
        return render(request, 'backend/pages/add_material.html', context)
        

def material_delete(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    return redirect('material_add')


def material_success(request):
    queryset = Material.objects.all()
    context = {
        'queryset':queryset
    }
    return render(request, 'backend/successed/material_success.html', context)


def storage_add(request):
    form = StorageForm()
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage_list')
    else:
        form = StorageForm()
        return render(request, 'backend/pages/add_storage.html', {'form':form})

def storage_list(request):
    queryset = Storage.objects.all()
    context = {'queryset':queryset}
    return render(request, 'backend/successed/storage_success.html', context)

