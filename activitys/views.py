from rest_framework import generics, renderers
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .models import Activity, ActivityCategory
from .serializers import ActivityCategorySerializer
from .permissions import IsOwnerOrReadOnly

#1. Root API Endpoint
@api_view(['GET'])
def activityscategorys_root(request, format=None ):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'activitys-categorys': reverse('activityscategory-list', request=request, format=format)
    })

class ActivityCategoryListAPIView(ListAPIView):
    #2. List activitys categories only view 
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
class ActivityCategoryListCreateAPIView(ListCreateAPIView):
    #3. List and create activitys view
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # serializer.save()
        # return super().perform_create(serializer)
class ActivityCategoryEditDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class ActivityCategoryDeleteAPIView(RetrieveDestroyAPIView):
#     queryset = ActivityCategory.objects.all
#     serializer_class = ActivityCategoryRetrieveDetailsSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

# class ActivityCategoryUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = ActivityCategory.objects.all
#     serializer_class = ActivityCategoryCreateUpdateSerializer
#     permission_classes = [IsAuthenticated, ]

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#         # return super().perform_update(serializer)

#     def update(self, request, pk,  *args, **kwargs):
#         activity = get_object_or_404(self.get_queryset(), pk=pk)
#         activity.save()
#         return super().update(request, *args, **kwargs)

# class ActivityCategoryRetrieveDetailsAPIView(RetrieveAPIView):
#     queryset = ActivityCategory.objects.all()
#     serializer_class = ActivityCategoryRetrieveDetailsSerializer


# class ActivityCategoryListAPIView(ListAPIView):
#     queryset = ActivityCategory.objects.all()
#     serializer_class = ActivityCategoryListSerializer



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


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'multipart/form-data'
#         super(JSONResponse, self).__init__(content, **kwargs)


#     @api_view(['GET', 'POST'])
#     def get_activity_category_list(request):
#         # Get a list of allActivity catagories
#         if request.method == 'GET':
#             activitys_category = ActivityCategory.objects.all()
#             activitys_serializer = ActivityCategorySerializer(activitys_category, many=True)
#             return Response(activitys_serializer.data)
#         # Insert a new Activity Catagory 
#         elif request.method == 'POST':
#             activitys_serializer = ActivityCategorySerializer(data=request.data)
#             if activitys_serializer.is_valid():
#                 activitys_serializer.save()
#                 return Response(activitys_serializer.data, status=status.HTTP_201_CREATED)
#             return Response(activitys_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @api_view(['GET', 'PUT', 'DELETE'])
#     def get_edit_delete_activitys(request, pk):
#         try:
#             activitys_category = ActivityCategory.objects.get(pk=pk)
#         except ActivityCategory.DoesNotExist:
#             return Response(ststus=status.HTTP_404_NOT_FOUND)
#         if request.method == 'GET':
#             activitys_serializer = ActivityCategorySerializer(activitys_category)
#             return Response(activitys_serializer.data)
#         elif request.method == 'PUT':
#             activitys_serializer = ActivityCategorySerializer(activitys_category, data=request.data)
#             if activitys_serializer.is_valid():
#                 activitys_serializer.save()
#                 return Response(activitys_serializer.data)
#             return Response(activitys_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             activitys_category.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
