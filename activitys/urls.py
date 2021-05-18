from django.conf.urls import include, url
from django.db import router
from django.urls import path, include
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from activitys import views
from activitys.views import ActivitysCategorysViewSet, ActivitysViewSet
# from users import views
# from users.views import UserViewSet


# Create a router and register the viewsets with it
router = SimpleRouter()
router.register(r'activityscategorys', views.ActivitysCategorysViewSet)
router.register(r'activitys', views.ActivitysViewSet)
# router.register(r'users', views.UserViewSet)


# activityscategorys_list = ActivitysCategorysViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# activityscategorys_detail = ActivitysCategorysViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# URL patterns are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),

    # path('activitys/', activityscategorys_list, name='activityscategory-list'),
    # path('activitys/create/', views.ActivityCategoryListCreateAPIView.as_view()),
    # path('activitys/<int:pk>/', activityscategorys_detail, name='activityscategory-detail'),
    # path('activitys/<int:pk>/detail/', activityscategorys_detail,  name='activityscategory-id')

    # path('activitys/', views.ActivityCategoryListAPIView.as_view(), name='activityscategory-list'),
    # path('activitys/create/', views.ActivityCategoryListCreateAPIView.as_view()),
    # path('activitys/<int:pk>/', views.ActivityCategoryEditDeleteAPIView.as_view(), name='activityscategory-detail'),
    # path('activitys/<int:pk>/detail/', views.ActivityCategoryEditDeleteAPIView.as_view(), name='activityscategory-id')

]

# urlpatterns = format_suffix_patterns(urlpatterns)


