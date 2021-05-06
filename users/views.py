from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User
from activitys.models import ActivityCategory
from .serializers import UserSerializer

# Create your views here.

#1. Root API Endpoint
@api_view(['GET'])
def users_root(request, format=None ):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        # 'activitys-categorys': reverse('activityscategorys-list', request=request, format=format)
    })

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


