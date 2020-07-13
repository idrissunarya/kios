from rest_framework import serializers
from .models import Material, Member

#class MaterialSerializer(serializers.HyperlinkedModelSerializer):
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'username', 'created']