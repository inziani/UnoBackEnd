from django.contrib import admin
from .models import Activity, ActivityCategory

# Register your models here.

activityModels = [Activity, ActivityCategory]

admin.site.register(activityModels)