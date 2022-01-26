from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)

# Create your views here.

from .models import GLDocument, GLAccountLineItems

class GLDocumentViewSet(viewsets.ModelViewSet):
    queryset = GLDocument.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GLAccountLineItemsViewSet(viewsets.ModelViewSet):
    queryset = GLAccountLineItems.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
