from django.db import router
from django.urls import path, include, re_path

from rest_framework import viewsets
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import GLAccountLineItemsViewSet, GLDocumentViewSet

# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'glLineItems', views.GLAccountLineItemsViewSet)
router.register(r'glDocument', views.GLDocumentViewSet)

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]