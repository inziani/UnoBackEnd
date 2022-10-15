from django.shortcuts import render
# from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, UserProfile, EmployeeBankInformation, EmployeeIDInformation, EmployeeBankInformation, EmployeeMaritalInformation, EmployeeDependants, EmployeeNextOfKin
from activitys.models import ActivityCategory
from .serializers import UserSerializer, UserProfileSerializer, RegistrationSerializer, CustomTokenObtainPairSerializer, EmployeeIDInformationSerializer, EmployeeMaritalInformationSerializer, EmployeeNextOfKinSerializer, EmployeeDependantsSerializer, EmployeeBankInformationSerializer


# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    # queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This Viewset automatically provides list and retrieve actions - ReadOnlyModelViewSet"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """This Viewset automatically provides list and retrieve actions - ReadOnlyModelViewSet"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class EmployeeIDInformationViewSet(viewsets.ReadOnlyModelViewSet):
    """This Viewset automatically provides list and retrieve actions - ReadOnlyModelViewSet"""
    queryset = EmployeeIDInformation.objects.all()
    serializer_class = EmployeeIDInformationSerializer
    permission_classes = [IsAuthenticated]

class EmployeeNextOfKinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeNextOfKin.objects.all()
    serializer_class = EmployeeNextOfKinSerializer
    permission_classes = [IsAuthenticated]

class EmployeeMaritalInformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeMaritalInformation.objects.all()
    serializer_class = EmployeeMaritalInformationSerializer
    permission_classes = [IsAuthenticated]

class EmployeeDependantsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeDependants.objects.all()
    serializer_class = EmployeeDependantsSerializer
    permission_classes = [IsAuthenticated]

class EmployeeBankInformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeBankInformation.objects.all()
    serializer_class = EmployeeBankInformationSerializer
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






    


