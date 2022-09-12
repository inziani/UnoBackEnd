from django.contrib import admin

from .models import TaxCode, GeneralLedgerAccountGroup, GeneralLedgerAccountMaster

# Register your models here.
masterDataModels = [TaxCode, GeneralLedgerAccountGroup, GeneralLedgerAccountMaster]

admin.site.register(masterDataModels)
