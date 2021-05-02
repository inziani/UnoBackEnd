from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth import get_user_model
from .constants import CATEGORY, STATUS

# Create your models here.

class ActivityCategory(models.Model):
    description = models.CharField(max_length=155)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    # change_by = 
    category = models.CharField(choices=CATEGORY, default='',max_length=155)

    class Meta:
        ordering = ('description', )
    
    def __str__(self):
        return self.description


class Activity(models.Model):

    class ActivitysObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = ['Created', 'Progress'])

    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=155, blank=False, default='Activity Description')
    details = models.CharField(max_length=300, blank=False, default='Activity Details')
    activity_category = models.ForeignKey(ActivityCategory, related_name='activitys', on_delete=PROTECT)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='activitys', default=1)
    slug = models.SlugField(max_length=250, unique_for_date='date_created', default='slug')
    status = models.CharField(choices=STATUS,  max_length=30, default='Created')
    objects = models.Manager()
    activitysobjects = ActivitysObjects()

    # Check whethere the default owner will be overwritten by the perform_create function in the serializer.

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return f'{self.description}, {self.owner}'

    def create(self, ):
        return self.save()

    def change(self, description, details, activity_category ):
        self.description = description
        self.details = details
        self.activity_category = activity_category
        return self.save()

    def delete(self, ):
        return self.delete()

