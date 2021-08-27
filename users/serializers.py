
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User, UserProfile
from activitys.models import ActivityCategory, Activity

class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password',)

class RegistrationSerializer(HyperlinkedModelSerializer):
    """ Serializer registration requests and creates new user"""
    password = serializers.CharField(
        max_length = 128,
        min_length = 12,
        write_only = True
    )

    # The client should not be able to send a token along with a registration request. Make the request readonly to handle it.
    token = serializers.CharField(max_length=255, read_only = True)

    class Meta:
        model = User
        # List all the fields that could possible be included in a request or response including fields specified explicitly above
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the create_user method to create new user
        return User.objects.create_user(**validated_data)
    