
from django.db import router
from django.urls import path, include, re_path
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter


from company.views import CompanyViewSet, CompanyCodeViewSet, ChartOfAccountsViewSet, ReportingAreaViewSet, ControllingAreaViewSet, BusinessAreaViewSet
from company import views


# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'companyCode', views.CompanyCodeViewSet)
router.register(r'chartOfAccounts', views.ChartOfAccountsViewSet)
router.register(r'reportingArea', views.ReportingAreaViewSet)
router.register(r'controllingArea', views.ControllingAreaViewSet)
router.register(r'businessArea', views.BusinessAreaViewSet)

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




