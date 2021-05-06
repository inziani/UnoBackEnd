# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User, UserProfile
from activitys.models import ActivityCategory, LANGUAGE_CHOICES, STYLE_CHOICES

class UserSerializer(HyperlinkedModelSerializer):
    # activityscategorys = serializers.PrimaryKeyRelatedField(many=True,= queryset=ActivityCategory.objects.all()) 
    activityscategorys = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'activityscategorys')