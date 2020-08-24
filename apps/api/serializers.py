from rest_framework import serializers
from .models import Material, Member, Storage, Location

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