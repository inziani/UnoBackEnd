
from django.db import router
from django.urls import path, include, re_path
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import GLAccountBalancesViewSet
from accountbalances import views

router = SimpleRouter()
router.register(r'glAccountBalances', views.GLAccountBalancesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
