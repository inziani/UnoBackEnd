from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    date_created = serializers.DateTimeField()
    date_changed = serializers.DateTimeField()
    description = serializers.CharField(max_length=155)
    details = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.details = validated_data.get('details', instance.details)
        instance.save
        return super().update(instance, validated_data)


