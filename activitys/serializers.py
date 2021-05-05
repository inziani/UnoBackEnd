
from users.serializers import serializers
from rest_framework.serializers import ModelSerializer
from activitys.models import ActivityCategory, Activity, LANGUAGE_CHOICES, STYLE_CHOICES


class ActivityCategorySerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ActivityCategory
        fields = ('id', 'title', 'description', 'category','date_created', 'date_changed', 'owner', 'language', 'style' )

