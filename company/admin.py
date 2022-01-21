from django.contrib import admin

from models import CompanyCode, Company, ChartOfaccounts

# Register your models here.

companyModels = [Company, CompanyCode, ChartOfaccounts, ReportingArea]

admin.site.register(companyModels)


