from rest_framework import serializers
from rest_framework.generics import (DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)



from activitys.models import Activity, ActivityCategory
from activitys.serializers import (ActivityCategoryListSerializer, ActivityCategoryRetrieveDetailsSerializer, ActivityCategoryCreateUpdateSerializer)


class ActivityCategoryCreateAPIView(CreateAPIView):
    queryset = ActivityCategory.objects.all
    serializer_class = ActivityCategoryCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        serializer.save()
    #     # return super().perform_create(serializer)

class ActivityCategoryDeleteAPIView(DestroyAPIView):
    queryset = ActivityCategory.objects.all
    serializer_class = ActivityCategoryRetrieveDetailsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ActivityCategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ActivityCategory.objects.all
    serializer_class = ActivityCategoryCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg  = 'id'
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        # return super().perform_update(serializer)

class ActivityCategoryRetrieveDetailsAPIView(RetrieveAPIView):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategoryRetrieveDetailsSerializer


class ActivityCategoryListAPIView(ListAPIView):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategoryListSerializer



# from django.shortcuts import render
# from django.views import generic
# from rest_framework.generics import ListAPIView
# from rest_framework import generics, serializers
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from .models import ActivityCategory, Activity
# from .serializers import ActivitysCategorySerilaizer, ActivitysSerializer

# # Create your views here.

# class ActivitysCategoryList(generics.ListCreateAPIView):
#     queryset = ActivityCategory.objects.all()
#     serializer_class = ActivitysCategorySerilaizer
#     name = 'activitycategory-list'
    

# class ActivitysCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ActivityCategory.objects.all()
#     serializer_class = ActivitysCategorySerilaizer
#     name = 'activitycategory-detail'

# class ActivitysList(generics.ListCreateAPIView):
#     queryset = Activity.objects.all()
#     serializers_class = ActivitysSerializer
#     name = 'activity-list'

# class ActivityDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitysSerializer
#     name = 'activity-detail'

# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'activitys-categories': reverse(ActivitysCategoryList.name, request=request),
#             'activitys': reverse(ActivitysList.name, request=request)
#         })
