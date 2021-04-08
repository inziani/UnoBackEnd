from django.db import models

# Create your models here.

class Tasks(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=155, blank=False, default='Task Description')
    details = models.CharField(max_length=300, blank=False, default='Task Details')

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.description

    def create(self, ):
        return self.save()

    def change(self,description, details ):
        self.description = description
        self.details = details
        return self.save()

    def delete(self, ):
        return self.delete()

