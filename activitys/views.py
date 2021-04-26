from django.shortcuts import render
from django.views import generic
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import ActivityCategory, Activity
from .serializers import ActivitysCategorySerilaizer, ActivitysSerializer

# Create your views here.

class ActivitysCategoryList(generics.ListCreateAPIView):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivitysCategorySerilaizer
    name = 'activitycategory-list'

class ActivitysCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivitysCategorySerilaizer
    name = 'activitycategory-detail'

class ActivitysList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializers_class = ActivitysSerializer
    name = 'activity-list'

class ActivityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitysSerializer
    name = 'activity-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'activitys-categories': reverse(ActivitysCategoryList.name, request=request),
            'activitys': reverse(ActivitysList.name, request=request)
        })
