from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model
from decimal import Decimal

from company.constants import CURRENCY
from company.models import ChartOfaccounts, CompanyCode
from .constants import RECONACCOUNT

# Create your models here.

class TaxCode(models.Model):
    companyCode = models.ForeignKey(CompanyCode, related_name='companyCode_TaxCode', on_delete=PROTECT)
    taxCode = models.CharField(max_length=2, null=False, blank=False, unique=True)
    taxCodeDescription = models.CharField(max_length=50, null=False, blank=False)
    taxCodePercentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'), blank=False, null=False, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('taxCode',)

    def __str__(self):
        return f'{self.companyCode}, {self.taxCode}, {self.taxCodeDescription}, {self.taxCodePercentage}'

    def create(self, ):
        return self.save()
    
    def change(self, taxCodeDescription, taxCodePercentage):
        self.taxCodeDescription = taxCodeDescription
        self.taxCodePercentage = taxCodePercentage
        return self.save()

class GLAccountGroup(models.Model):
    companyCode = models.ForeignKey(CompanyCode, related_name='companyCode_GLAccountGroup', on_delete=PROTECT)
    chartOfAccounts = models.ForeignKey(ChartOfaccounts, related_name='glAccountGroup', on_delete=PROTECT)
    accountGroup = models.CharField(max_length=4, null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    fromAccount = models.IntegerField(null=False, blank=False, unique=True)
    toAccount = models.IntegerField(null=False, blank=False, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('chartOfAccounts',)

    def __str__(self):
        return f'{self.companyCode}, {self.chartOfAccounts}, {self.description}'

    def create(self, ):
        return self.save()
    
    def change(self, chartOfAccounts, description, fromAccount,  toAccount):
        self.chartOfAccounts = chartOfAccounts
        self.description = description
        self.fromAccount = fromAccount
        self.toAccount = toAccount
        return self.save()

class GeneralLedgeAccountMaster(models.Model):
    accountNumber = models.IntegerField(null=False, blank=False, unique=True)
    companyCode = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, related_name='GeneralLedgeAccountMaster', on_delete=PROTECT)
    glAccountGroup = models.ForeignKey(GLAccountGroup, max_length=4, null= False, blank=True, related_name='GeneralLedgeAccountMaster', on_delete=PROTECT)
    profitAndLossAccount = models.BooleanField()
    balanceSheetAccount = models.BooleanField()
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=135)
    accountCurrency = models.CharField(choices=CURRENCY, null=False, blank=False, max_length=3)
    balancesLocalCurrency = models.BooleanField()
    exchangeRateDiffKey = models.CharField(max_length=3)
    taxCategory = models.CharField(max_length=2)
    taxableItem = models.BooleanField()
    reconciliationAccountType = models.CharField(choices=RECONACCOUNT, null=False, blank=False, max_length=30)
    openItemMgt = models.BooleanField()
    lineItemDisplay = models.BooleanField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('accountNumber',)

    def __str__(self):
        return f'{self.companyCode}, {self.accountNumber}, {self.shortDescription}'

    def create(self, ):
        return self.save()
    
    def change(self , 
    companyCode, glAccountGroup, profitAndLossAccount, balanceSheetAccount, shortDescription, 
    longDescription, accountCurrency, balancesLocalCurrency, exchangeRateDiffKey , taxCategory,  
    taxableItem, reconciliationAccountType, openItemMgt,  lineItemDisplay):
        self.companyCode = companyCode
        self.glAccountGroup = glAccountGroup
        self.profitAndLossAccount = profitAndLossAccount
        self.balanceSheetAccount = balanceSheetAccount
        self.shortDescription = shortDescription
        self.longDescription = longDescription
        self.accountCurrency = accountCurrency
        self.accountCurrency = accountCurrency
        self.balancesLocalCurrency = balancesLocalCurrency
        self.exchangeRateDiffKey = exchangeRateDiffKey
        self.taxCategory = taxCategory
        self.taxableItem = taxableItem
        self.reconciliationAccountType = reconciliationAccountType
        self.openItemMgt = openItemMgt
        self.lineItemDisplay = lineItemDisplay
        return self.save()







