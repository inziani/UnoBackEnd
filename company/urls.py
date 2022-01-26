
from django.db import router
from django.urls import path, include, re_path
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter


from company.views import CompanyViewSet, CompanyCodeViewSet, ChartOfaccountsViewSet, ReportingAreaViewSet


# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'companyCode', views.CompanyCodeViewSet)
router.register(r'chartOfAccounts', views.ChartOfaccountsViewSet)
router.register(r'reportingArea', views.ReportingAreaViewSet)

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




