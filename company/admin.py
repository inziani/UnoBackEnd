from django.contrib import admin

from .models import CompanyCode, Company, ChartOfAccounts, ReportingArea

# Register your models here.

companyModels = [Company, CompanyCode, ChartOfAccounts, ReportingArea]

admin.site.register(companyModels)


