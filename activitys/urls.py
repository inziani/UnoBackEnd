from django.conf.urls import url
from django.urls import path

from .views import ActivitysList, ActivityDetails, ActivitysCategoryList, ActivitysCategoryDetail, ApiRoot

urlpatterns = [
    path('activitycategory-detail/', ActivitysCategoryList.as_view()),
    path('activity-list/', ActivitysList.as_view()),
    path('api-root/',ApiRoot.as_view()),
]