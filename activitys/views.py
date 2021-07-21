from rest_framework import generics, renderers
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets


from .models import Activity, ActivityCategory
from .serializers import ActivityCategorySerializer, ActivitySerializer
from .permissions import IsOwnerOrReadOnly
from activitys import permissions


    # Refactor the generic class based views to use viewsets and routers and Hyperlinkedserialisers
class ActivitysCategorysViewSet(viewsets.ModelViewSet):
    """ This view set automatically provides for list, create, retrieve update and destory actions"""
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ActivitysViewSet(viewsets.ModelViewSet):
    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


