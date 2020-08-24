from django.contrib import admin
from . models import Product, Member, Storage, Material, Location

class ProductModelAdmin (admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = Product
admin.site.register(Product, ProductModelAdmin)

class MemberModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    class Meta:
        model = Member
admin.site.register(Member, MemberModelAdmin)

class StorageModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'unit', 'qty']
    class Meta:
        model = Storage
admin.site.register(Storage, StorageModelAdmin)

class MaterialModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'name']
    class Meta:
        model = Material
admin.site.register(Material, MaterialModelAdmin)

class LocationModelAdmin(admin.ModelAdmin):
    list_display = ['city', 'city_ascii', 'country', 'iso2', 'iso3', 'admin_name', 'capital', 'population']
    class Meta:
        model = Location
admin.site.register(Location, LocationModelAdmin)