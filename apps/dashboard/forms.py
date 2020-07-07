from django import forms
from apps.api.models import Member, Material, Storage

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


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['name', 'unit', 'qty']

        def clean_name(self):
            name = self.cleaned_data.get('name')

            return name
