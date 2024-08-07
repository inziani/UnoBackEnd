"""onlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from rest_framework_simplejwt.views  import (TokenObtainPairView, TokenRefreshView, )
from django.conf import settings
from django.conf.urls.static import static




class OnlineShopDefaultRouter(routers.DefaultRouter):
    """Extends 'DefaultRouter' class to add a method to extend url routes from other routers"""
    def extend(self, router):
        """Extend the routes with url routes of the passed in router
        Args: 
            router: SimpleRouter instance containing route definitions
        """
        self.registry.extend(router.registry)

router = OnlineShopDefaultRouter()
from users.urls import router as users_router
router.extend(users_router)
from activitys.urls import router as activitys_router
router.extend(activitys_router)
from accountbalances.urls import router as accountBalances_router
router.extend(accountBalances_router)
from accountitems.urls import router as accountitems_router
router.extend(accountitems_router)
from company.urls import router as company_router
router.extend(company_router)
from masterdata.urls import router as glmasterdata_router
router.extend(glmasterdata_router)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
