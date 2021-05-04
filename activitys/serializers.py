from rest_framework.serializers import ModelSerializer
from activitys.models import ActivityCategory, Activity


class ActivityCategorySerializer(ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'

