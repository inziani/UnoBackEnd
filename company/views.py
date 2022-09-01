from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets

# Create your views here.


from .models import Company, CompanyCode, ChartOfAccounts, ReportingArea, ControllingArea, BusinessArea
from .serializers import CompanySerializer, CompanyCodeSerializer, ChartOfAccountsSerializer, ReportingAreaSerializer, ControllingAreaSerializer, BusinessAreaSerializer 
from activitys.permissions import IsOwnerOrReadOnly



    # Refactor the generic class based views to use viewsets and routers and Hyperlinkedserialisers
class CompanyViewSet(viewsets.ModelViewSet):
    """ This view set automatically provides for list, create, retrieve update and destory actions"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class CompanyCodeViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()


class ChartOfAccountsViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()

class ReportingAreaViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = ReportingArea.objects.all()
    serializer_class = ReportingAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()

class ControllingAreaViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = ControllingArea.objects.all()
    serializer_class = ControllingAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()

class BusinessAreaViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = BusinessArea.objects.all()
    serializer_class = BusinessAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save()



