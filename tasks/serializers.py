from rest_framework import serializers
from tasks.models import Tasks


class TasksSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    date_created = serializers.DateTimeField()
    date_changed = serializers.DateTimeField()
    description = serializers.CharField(max_length=155)
    details = serializers.CharField(max_length=300)


