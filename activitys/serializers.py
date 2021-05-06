from users.serializers import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from activitys.models import ActivityCategory, Activity, LANGUAGE_CHOICES, STYLE_CHOICES


class ActivityCategorySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.HyperlinkedIdentityField(view_name='activityscategory-title', format='html')
    class Meta:
        model = ActivityCategory
        fields = ('id', 'title', 'description', 'category','date_created', 'date_changed', 'owner', 'language', 'style')


