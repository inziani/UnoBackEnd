# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, UserProfile
from activitys.models import ActivityCategory, LANGUAGE_CHOICES, STYLE_CHOICES

class UserSerializer(ModelSerializer):
    activityscategorys = serializers.PrimaryKeyRelatedField(many=True, queryset=ActivityCategory.objects.all()) 

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'middle_name', 'last_name', 'activityscategorys')