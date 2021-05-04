from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from activitys import views

urlpatterns = [

    path('activitys/', views.ActivityCategoryListAPIView.as_view()),
    path('activitys/create/', views.ActivityCategoryListCreateAPIView.as_view()),
    path('activitys/<int:pk>/', views.ActivityCategoryEditDeleteAPIView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)

# url(r'^', views.JSONResponse.get_activity_category_list),
# url(r'^(?P<pk>[0-9]+)/', views.JSONResponse.get_edit_delete_activitys)
