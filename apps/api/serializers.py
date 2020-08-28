from rest_framework import serializers
from .models import Material, Member, Storage, Location, Currency, USA

#class MaterialSerializer(serializers.HyperlinkedModelSerializer):
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'created', 'updated']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'username', 'created']

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['name', 'unit', 'qty', 'created']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class USASerializer(serializers.ModelSerializer):
    class Meta:
        model = USA
        fields = '__all__'