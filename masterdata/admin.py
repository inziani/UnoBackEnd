from django.contrib import admin

from .models import GeneralLedgerAccountMaster

# Register your models here.
masterDataModels = [GeneralLedgerAccountMaster]

admin.site.register(masterDataModels)
