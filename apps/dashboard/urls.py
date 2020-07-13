from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
from .views import MaterialListView, MemberListView

#router = routers.DefaultRouter()
#router.register('materials', views.MaterialViewSet)


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('storage/', views.storage, name='storage'),
    path('storage_list/', views.storage_list, name='storage_list'),
    path('material/', views.material, name='material'),

    path('api-material/', MaterialListView.as_view(), name='material-all'),
    path('api-member/', MemberListView.as_view(), name='member-all')

]
