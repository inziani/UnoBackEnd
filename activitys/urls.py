from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from activitys.views import ActivityCategoryListAPIView
app_name = 'activitys'

urlpatterns = [
    # url(r'^$', ActivityCategoryListAPIView.as_view(), name='activity-list')
    path('', ActivityCategoryListAPIView.as_view(), name='activitys-list')
]

# from django.urls import path
# from activitys import views
# from rest_framework import views

# from .views import ActivitysList, ActivityDetails, ActivitysCategoryList, ActivitysCategoryDetail, ApiRoot

# urlpatterns = [
#     path('', ActivitysCategoryList.as_view()),

# ]