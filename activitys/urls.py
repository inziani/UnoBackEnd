from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from activitys import views
import activitys

urlpatterns = [

    path('activitys/', views.ActivityCategoryListAPIView.as_view(), name='activityscategory-list'),
    path('activitys/create/', views.ActivityCategoryListCreateAPIView.as_view()),
    path('activitys/<int:pk>/', views.ActivityCategoryEditDeleteAPIView.as_view(), name='activityscategory-detail'),
    path('activitys/<int:pk>/hyperlinked/', views.ActivityCategoryEditDeleteAPIView.as_view(), name='activityscategory-title')

]

urlpatterns = format_suffix_patterns(urlpatterns)


