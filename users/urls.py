from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from users import views
from users.views import UserViewSet

router = SimpleRouter()
router.register(r'users', views.UserViewSet)

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    path('', include(router.urls))

#     # path('users/', views.UserList.as_view(), name='user-list'),
#     # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')

#     # path('users/', user_list,  name='user-list'),
#     # path('users/<int:pk>/', user_detail, name='user-detail')

]

# urlpatterns = format_suffix_patterns(urlpatterns)