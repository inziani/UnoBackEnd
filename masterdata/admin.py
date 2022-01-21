from django.contrib import admin

from models import TaxCode, GLAccountGroup, GeneralLedgeAccountMaster

# Register your models here.
masterDataModels = [TaxCode, GLAccountGroup, GeneralLedgeAccountMaster]

admin.site.register(masterDataModels)
