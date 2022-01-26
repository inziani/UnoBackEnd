from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)

from .models import GLAccountBalances
from .serializers import GLAccountBalancesSerializer
from activitys.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

# Create your views here.

class GLAccountBalancesViewSet(viewsets.ModelViewSet):
    queryset = GLAccountBalances.objects.all()
    serializer_class = GLAccountBalancesSerializer
    permission_classes =[ IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

