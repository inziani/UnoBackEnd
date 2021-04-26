from django.contrib import admin
from tasks.models import Task, TaskCategory

# Register your models here.

tasksModels = [Task, TaskCategory]
admin.site.register(tasksModels)
