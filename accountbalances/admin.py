from django.contrib import admin

from models import GLAccountBalances


# Register your models here.

accountBalancesModels = [GLAccountBalances]

admin.site.register(accountBalancesModels)
