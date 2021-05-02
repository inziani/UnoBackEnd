from django.conf.urls import url
from activitys import views

urlpatterns = [

    url(r'^', views.JSONResponse.get_activity_category_list),
    url(r'^(?P<pk>[0-9]+)/', views.JSONResponse.get_edit_delete_activitys)

]
