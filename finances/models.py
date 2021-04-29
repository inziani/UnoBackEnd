from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from .constants import CATEGORY

# Create your models here.

class TaskCategory(models.Model):
    description = models.CharField(max_length=155)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=CATEGORY, default='',max_length=155)

    class Meta:
        ordering = ('description', )
    
    def __str__(self):
        return self.description

    def create(self, ):
        return self.save()

    def change(self, description, category ):
        self.description = description
        self.category = category
        return self.save()

    def delete(self, ):
        return self.delete()


class Task(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=155, blank=False, default='Task Description')
    details = models.CharField(max_length=300, blank=False, default='Task Details')
    task_category = models.ForeignKey(TaskCategory, related_name='tasks', on_delete=CASCADE, default=0)
    
    

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.description

    def create(self, ):
        return self.save()

    def change(self, description, details ):
        self.description = description
        self.details = details
        # self.task_catagory = task_catagory
        return self.save()

    def delete(self, ):
        return self.delete()

