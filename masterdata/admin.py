from django.contrib import admin

from .models import TaxCode, GLAccountGroup, GeneralLedgerAccountMaster

# Register your models here.
masterDataModels = [TaxCode, GLAccountGroup, GeneralLedgerAccountMaster]

admin.site.register(masterDataModels)
