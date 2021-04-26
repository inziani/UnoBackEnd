from rest_framework import serializers
from .models import ActivityCategory, Activity
from . import views
import activitys


class ActivitysCategorySerilaizer(serializers.HyperlinkedModelSerializer):
    activitys = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='activity-detail')

    class Meta:
        model = ActivityCategory
        fields = ('url', 'pk', 'description', 'activitys')

class ActivitysSerializer(serializers.HyperlinkedModelSerializer):
    activitys_category = serializers.SlugRelatedField(queryset=ActivityCategory.objects.all(), slug_field='description')

    class Meta:
        model = Activity
        fields = ('url', 'details', 'description', 'activity_category')