from rest_framework.serializers import ModelSerializer
from activitys.models import ActivityCategory, Activity


class ActivityCategoryCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ['id', 'description', 'category', 'date_created']
        

class ActivityCategoryListSerializer(ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'

class ActivityCategoryRetrieveDetailsSerializer(ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'





# class ActivitysCategorySerilaizer(serializers.HyperlinkedModelSerializer):
#     activitys = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='activity-detail')

#     class Meta:
#         model = ActivityCategory
#         fields = ('url', 'pk', 'description', 'category', 'activitys')

# class ActivitysSerializer(serializers.HyperlinkedModelSerializer):
#     activitys_category = serializers.SlugRelatedField(queryset=ActivityCategory.objects.all(), slug_field='description')

#     class Meta:
#         model = Activity
#         fields = ('url', 'details', 'description', 'activity_category', 'owner')