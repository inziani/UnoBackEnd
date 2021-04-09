from django.contrib import admin
from tasks.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    model = Task
    fields = ('description', 'details' )


admin.site.register(Task, TaskAdmin)
