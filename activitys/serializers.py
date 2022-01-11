from users.serializers import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from activitys.models import ActivityCategory, Activity



class ActivityCategorySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ActivityCategory
        fields = ('url', 'id', 'title', 'description', 'category','date_created', 'date_changed', 'owner')


class ActivitySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # category = serializers.ReadOnlyField(source='activity_category.id', read_only=True)
    # activity_category = serializers.ForeignKeyRelatedField(read_only=True)

    class Meta:
        model = Activity
        # fields = '__all__'
        fields =  ('url', 'owner', 'id', 'title', 'description', 'status','date_created', 'date_changed', 'activity_category')

class ActivityUpdateSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(source='activity_category', read_only=True)

    class Meta:
        model = Activity
        fields = ('url', 'owner', 'id', 'title', 'description', 'status','date_created', 'date_changed', 'activity_category', 'category')
