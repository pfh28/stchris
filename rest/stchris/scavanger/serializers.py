from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Hunt, Treasure


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = ['name', 'description', 'point_value', 'limit']

class HuntSerializer(serializers.ModelSerializer):
    treasures = TreasureSerializer(many = True)
    class Meta:
        model = Hunt
        fields = ['name', 'treasures']
