# from django.conf.urls import url
# from django.urls import include, re_path
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from users import views
from users.views import UserViewSet, RegistrationViewSet, UserProfileViewSet

router = SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'user-profile', views.UserProfileViewSet)
router.register(r'register', views.RegistrationViewSet)


urlpatterns = [
    # path('', include(router.urls))
    # re_path(r'^$', home, name='home'),
    # re_path(r'^myapp/', include('myapp.urls'),
    re_path(r'^', include(router.urls))

]
