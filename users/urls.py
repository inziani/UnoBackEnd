
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from users import views
from users.views import UserViewSet, RegistrationViewSet, UserProfileViewSet, EmployeeIDInformationViewSet, EmployeeNextOfKinViewSet,  EmployeeMaritalInformationViewSet, EmployeeDependantsViewSet, EmployeeBankInformationViewSet

router = SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'user-profile', views.UserProfileViewSet)
router.register(r'empIDInfo', views.EmployeeIDInformationViewSet)
router.register(r'empKinInfo', views.EmployeeNextOfKinViewSet)
router.register(r'empMaritalInfo', views.EmployeeMaritalInformationViewSet)
router.register(r'empDepInfo', views.EmployeeDependantsViewSet)
router.register(r'empBankInfo', views.EmployeeBankInformationViewSet)
router.register(r'register', views.RegistrationViewSet)


urlpatterns = [
    
    re_path(r'^', include(router.urls))

]
