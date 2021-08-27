from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, status

from .models import User
from activitys.models import ActivityCategory
from .serializers import UserSerializer, RegistrationSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This Viewset automatically provides list and retrieve actions - ReadOnlyModelViewSet"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    # Allow any user (authenticated or not) to hit this endpoint
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    # http_method_names = ['post', 'head']

    def post(self,request):
        user = request.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)






    


