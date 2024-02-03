from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets

# Create your views here.

from .models import GeneralLedgerAccountMaster, TaxCode, GeneralLedgerAccountGroup 
from .serializers import GeneralLedgerAccountMasterSerializer, TaxCodeSerializer, GeneralLedgerAccountGroupSerializer
# from activitys.permissions import IsOwnerOrReadOnly

class TaxCodeViewSet(viewsets.ModelViewSet):
    """ This view set automatically provides for list, create, retrieve update and destory actions"""
    queryset = TaxCode.objects.all()
    serializer_class = TaxCodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class GLAccountGroupViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = GeneralLedgerAccountGroup.objects.all()
    serializer_class = GeneralLedgerAccountGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class GeneralLedgerAccountMasterViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = GeneralLedgerAccountMaster.objects.all()
    serializer_class = GeneralLedgerAccountMasterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()
        # serializer.save(owner=self.request.user)
