from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from users import views
from users.views import UserViewSet, RegistrationViewSet, UserProfileViewSet

router = SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'user-profile', views.UserProfileViewSet)
router.register(r'register', views.RegistrationViewSet)


urlpatterns = [
    path('', include(router.urls))

]
