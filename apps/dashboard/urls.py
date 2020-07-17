from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
from .views import MaterialListView, MemberListView, StorageListView


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('storage_add/', views.storage_add, name='storage_add'),
    path('storage_list/', views.storage_list, name='storage_list'),
    path('material_add/', views.material_add, name='material_add'),
    path('material_delete/', views.material_delete, name='material_delete'),
    path('material_success/', views.material_success, name='material_success'),

    # Apis localhost
    path('api-material/', MaterialListView.as_view(), name='material-all'),
    path('api_material/<str:id>', views.api_material, name='api_material'),
    path('delete_material/<str:id>', views.delete_material, name='delete_material'),
    path('api-member/', MemberListView.as_view(), name='member-all'),
    path('api-storage/', StorageListView.as_view(), name='storage-all')

]
