from django.contrib import admin
from . models import Product

class ProductModelAdmin (admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Product
