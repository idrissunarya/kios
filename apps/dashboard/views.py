from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, MaterialForm, StorageForm, LocationForm, CurrencyForm
from apps.api.models import Member, Storage, Material, Location, Currency, USA
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


from rest_framework import viewsets
from apps.api.serializers import MaterialSerializer, MemberSerializer, StorageSerializer, LocationSerializer, CurrencySerializer, USASerializer
from rest_framework import generics

from django.core import serializers
from django_tables2 import SingleTableView


# Class Serializer packages
class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all().order_by('-created')
    serializer_class = MaterialSerializer

class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all().order_by('-created')
    serializer_class = MemberSerializer

class StorageListView(generics.ListAPIView):
    queryset = Storage.objects.all().order_by('-created')
    serializer_class = StorageSerializer

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializer

class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all().order_by('id')
    serializer_class = CurrencySerializer

class USAListView(generics.ListAPIView):
    queryset = USA.objects.all().order_by('id')
    serializer_class = USASerializer

# def API List
def api_material(request, id):
    q = Material.objects.filter(id=id)
    serialized = serializers.serialize('json', q)
    return JsonResponse(serialized, safe=False)

def api_location(request, id):
    q = Location.objects.filter(id=id)
    serialized = serializers.serialize('json', q)
    return JsonResponse(serialized, safe=False)

def api_currency(request, id):
    q = Currency.objects.filter(id=id)
    serialized = serializers.serialize('json', q)
    return JsonResponse(serialized, safe=False)

def api_usa(request):
    q = USA.objects.all()
    serialized = serializers.serialize('json', q)
    return JsonResponse(serialized, safe=False)

# def Authenticated user login signup and register
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

# def CRUD Cities
def location_list(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
        queryset = Location.objects.all()
        context = {'queryset': queryset, 'form':form}
        return render(request, 'backend/pages/location_list.html', context)

def location_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_add')
    else:
        form = LocationForm()
        context = {'form': form}
        return render(request, 'backend/pages/add_location.html', context)

def delete_location(request,id):
    q = Location.objects.filter(id=id)
    q.delete()
    return JsonResponse({'status': 'success delete'}, safe=False)

def detail_location(request, id):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_add')
    else:
        queryset = Location.objects.get(id=id)
        form = LocationForm()
        context = {'queryset':queryset, 'form': form}
        return render(request, 'backend/pages/detail_location.html', context)

# def CRUD Currency
def currency_list(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        queryset = Currency.objects.all()
        form = CurrencyForm()
        context = {'queryset':queryset, 'form':form}
        return render(request, 'backend/pages/currency_list.html', context)

def currency_detail_json(request,id):
    currency = Currency.objects.all()
    q = list(currency)
    return JsonResponse(q, safe=False)

def currency_delete(request,id):
    currency = Currency.objects.filter(id=id)
    currency.delete()
    return JsonResponse({'status': 'success deleted'}, safe=False)

# def CRUD Materials
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

def delete_material(request,id):
    q = Material.objects.filter(id=id)
    q.delete()
    return JsonResponse({'status': 'success delete'}, safe=False)

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

# Def CRUD USA
def usa_list(request):
    queryset = USA.objects.all()
    context = {'queryset': queryset}
    return render(request, 'backend/pages/usa_list.html', context)

