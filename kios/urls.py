from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.web.urls')),
    path('', include('apps.dashboard.urls')),
    path('admin/', admin.site.urls),
]
