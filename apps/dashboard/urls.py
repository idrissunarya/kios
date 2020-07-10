from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('storage/', views.storage, name='storage'),
    path('storage_list/', views.storage_list, name='storage_list'),
    path('material/', views.material, name='material'),
]
