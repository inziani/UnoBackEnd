from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets

# Create your views here.


from .models import Company, CompanyCode, ChartOfaccounts, ReportingArea
from .serializers import CompanySerializer, CompanyCodeSerializer, ChartOfaccountsSerializer, ReportingAreaSerializer 
from activitys.permissions import IsOwnerOrReadOnly



    # Refactor the generic class based views to use viewsets and routers and Hyperlinkedserialisers
class CompanyViewSet(viewsets.ModelViewSet):
    """ This view set automatically provides for list, create, retrieve update and destory actions"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CompanyCodeViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChartOfaccountsViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = ChartOfaccounts.objects.all()
    serializer_class = ChartOfaccountsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReportingAreaViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides for list, create, retrieve, update and destroy actions
    """
    queryset = ReportingArea.objects.all()
    serializer_class = ReportingAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



