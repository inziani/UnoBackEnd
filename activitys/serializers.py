from users.serializers import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from activitys.models import ActivityCategory, Activity



class ActivityCategorySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # url = serializers.HyperlinkedIdentityField(view_name='activityscategory-id', format='html')
    class Meta:
        model = ActivityCategory
        fields = ('url', 'id', 'title', 'description', 'category','date_created', 'date_changed', 'owner')


class ActivitySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Activity
        # fields = ('url', 'id', 'slug', 'description', 'details', 'activity_category', 'status', 'objects', 'activitysobjects','owner', 'date_created', 'date_changed', 'owner')
        fields = '__all__'
