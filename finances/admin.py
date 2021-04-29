from django.contrib import admin
from finances.models import Task, TaskCategory

# Register your models here.

financesModels = [Task, TaskCategory]
admin.site.register(financesModels)
