
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User, UserProfile
from activitys.models import ActivityCategory, Activity

class UserSerializer(HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'middle_name', 'last_name')
        