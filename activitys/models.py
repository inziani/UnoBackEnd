from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from .constants import CATEGORY

# Create your models here.

class ActivityCategory(models.Model):
    description = models.CharField(max_length=155)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=CATEGORY, default='',max_length=155)

    class Meta:
        ordering = ('description', )
    
    def __str__(self):
        return self.description


class Activity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=155, blank=False, default='Activity Description')
    details = models.CharField(max_length=300, blank=False, default='Activity Details')
    activity_category = models.ForeignKey(ActivityCategory, related_name='activitys', on_delete=CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='activitys', default=1)
    

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

