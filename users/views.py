from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import Serializer
from .models import User
from activitys.models import ActivityCategory
from .serializers import UserSerializer

# Create your views here.

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


