from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets

# Create your views here.

from .models import TaxCode, GLAccountGroup, GeneralLedgeAccountMaster 
from .serializers import TaxCodeSerializer, GLAccountGroupSerializer, GeneralLedgeAccountMasterSerializer
from activitys.permissions import IsOwnerOrReadOnly

class TaxCodeViewSet(viewsets.ModelViewSet):
    """ This view set automatically provides for list, create, retrieve update and destory actions"""
    queryset = TaxCode.objects.all()
    serializer_class = TaxCodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GLAccountGroupViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = GLAccountGroup.objects.all()
    serializer_class = GLAccountGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GeneralLedgeAccountMasterViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = GeneralLedgeAccountMaster.objects.all()
    serializer_class = GeneralLedgeAccountMasterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
