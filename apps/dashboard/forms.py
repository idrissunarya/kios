from django import forms
from apps.api.models import Member, Material, Storage, Location, Currency

# Class Form
class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']
        widgets = {
            'password' : forms.PasswordInput()
        }
        def clean_username(self):
            username = self.cleaned_data.get('username')
            return username

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'username', 'email', 'password']
        def clean_username(self):
            username = self.cleaned_data.get('username')
            return username

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']
        def clean_name(self):
            name = self.cleaned_data.get('name')
            return name

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'city_ascii', 'lat', 'lng', 'country', 'iso2', 'iso3', 'admin_name', 'capital', 'population']
        def clean_city(self):
            city = self.cleaned_data.get('city')
            return city

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['country', 'currency', 'code', 'symbol']
        def clean_country(self):
            country = self.cleaned_data.get('country')
            return country

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['name', 'unit', 'qty']
        def clean_name(self):
            name = self.cleaned_data.get('name')
            return name
