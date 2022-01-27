from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)

# Create your views here.

from .models import GLDocument, GLAccountLineItems
from activitys.permissions import IsOwnerOrReadOnly
from .serializers import GLAccountLineItemsSerializer, GLDocumentSerializer

class GLDocumentViewSet(viewsets.ModelViewSet):
    queryset = GLDocument.objects.all()
    serializer_class = GLDocumentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GLAccountLineItemsViewSet(viewsets.ModelViewSet):
    queryset = GLAccountLineItems.objects.all()
    serializer_class = GLAccountLineItemsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
