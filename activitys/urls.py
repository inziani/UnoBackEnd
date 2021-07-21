from django.conf.urls import include, url
from django.db import router
from django.urls import path, include
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from activitys import views
from activitys.views import ActivitysCategorysViewSet, ActivitysViewSet


# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'activityscategorys', views.ActivitysCategorysViewSet)
router.register(r'activitys', views.ActivitysViewSet)

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




