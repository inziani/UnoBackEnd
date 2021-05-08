from users.serializers import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from activitys.models import ActivityCategory, Activity



class ActivityCategorySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # url = serializers.HyperlinkedIdentityField(view_name='activityscategory-id', format='html')
    class Meta:
        model = ActivityCategory
        fields = ('url', 'id', 'title', 'description', 'category','date_created', 'date_changed', 'owner')


