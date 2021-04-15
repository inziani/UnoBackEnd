from django.conf.urls import url
from django.urls import path
from tasks import views

urlpatterns = [

    path('', views.JSONResponse.task_list, name='task_list'),
    path('<int:pk>/', views.JSONResponse.task_detail, name='task_detail')
]