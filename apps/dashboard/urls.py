from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
from .views import MaterialListView, MemberListView, StorageListView, LocationListView, CurrencyListView, USAListView


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    # Apis localhost
    path('api-material/', MaterialListView.as_view(), name='material-all'),
    path('api_material/<str:id>', views.api_material, name='api_material'),
    path('api-location/', LocationListView.as_view(), name='location-all'),
    path('api_location/<int:id>/', views.api_location, name='api_location'),
    path('api-currency/', CurrencyListView.as_view(), name='currency-all'),
    path('api-member/', MemberListView.as_view(), name='member-all'),
    path('api-storage/', StorageListView.as_view(), name='storage-all'),
    path('api-usa/', USAListView.as_view(), name='usa-all'),
    path('api-usa-json/', views.api_usa, name='usaJSON'),

    # Crud URL Materials
    path('material_add/', views.material_add, name='material_add'),
    path('delete_material/<str:id>', views.delete_material, name='delete_material'),
    path('material_success/', views.material_success, name='material_success'),

    # Crud URL Location
    path('location_list/', views.location_list, name='location_list'),
    path('location_add/', views.location_add, name='location_add'),
    path('delete_location/<str:id>', views.delete_location, name='delete_location'),
    path('detail_location/<str:id>/', views.detail_location, name='detail_location'),

    # Crud URL Currency
    path('currency_list/', views.currency_list, name='currency_list'),
    path('currency_detail_json/<str:id>/', views.currency_detail_json, name='currency_detail_json'),
    path('currency_delete/<str:id>',views.currency_delete, name='currency_delete'),

    # Crud URL USA
    path('usa_list/', views.usa_list, name='usa_list'),

    # Crud URL Storage
    path('storage_add/', views.storage_add, name='storage_add'),
    path('storage_list/', views.storage_list, name='storage_list'),

]
