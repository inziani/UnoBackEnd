from django.contrib import admin

from models import GLDocument, GLAccountLineItems

# Register your models here.


accountItemsModels = [GLDocument, GLAccountLineItems]

admin.site.register(accountItemsModels)
