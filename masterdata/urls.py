
from django.db import router
from django.urls import path, include, re_path
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter


from masterdata.views import GeneralLedgerAccountMasterViewSet, TaxCodeViewSet, GLAccountGroupViewSet
from masterdata import views


# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'taxCodes', views.TaxCodeViewSet)
router.register(r'generalLedgerAccountGroup', views.GLAccountGroupViewSet)
router.register(r'generalLedgerAccountMaster', views.GeneralLedgerAccountMasterViewSet)

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




