from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from activitys import views

from activitys.views import (ActivityCategoryDeleteAPIView, ActivityCategoryListAPIView, ActivityCategoryRetrieveDetailsAPIView,ActivityCategoryUpdateAPIView, ActivityCategoryDeleteAPIView, ActivityCategoryCreateAPIView)
app_name = 'activitys'

urlpatterns = [

    path('', ActivityCategoryListAPIView.as_view(), name='activitys-list'),
    path('<int:pk>/', ActivityCategoryRetrieveDetailsAPIView.as_view(), name='activitys-detail'),
    path('create/', ActivityCategoryCreateAPIView.as_view(), name='activitys-create'),
    path('<int:id>/edit/', ActivityCategoryUpdateAPIView.as_view(), name='activitys-update'),


    
    # path('<int:pk>/delete/', ActivityCategoryDeleteAPIView.as_view(), name='activitys-delete'),
    # path('<int:pk>/edit/', ActivityCategoryUpdateAPIView.as_view(), name='activitys-update'),
    # url(r'^(?P<id>[0-9]+)/edit/$', views.ActivityCategoryUpdateAPIView.as_view(), name='activitys-update'),
    # path('<int:pk>/', ActivityCategoryRetrieveDetailsAPIView.as_view(), name='activitys-detail'),
    # path('create/', ActivityCategoryCreateAPIView.as_view(), name='activitys-create'),
    # path('', ActivityCategoryListAPIView.as_view(), name='activitys-list'),
    
    
    

]

# from django.urls import path
# from activitys import views
# from rest_framework import views

# from .views import ActivitysList, ActivityDetails, ActivitysCategoryList, ActivitysCategoryDetail, ApiRoot

# urlpatterns = [
#     path('', ActivitysCategoryList.as_view()),

# ]