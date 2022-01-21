from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model

from company.constants import CURRENCY

from masterdata.models import ChartOfaccounts, CompanyCode

# Create your models here.

class TaxCode(models.Model):
    taxCode = model.CharField(max_length=2, null=False, blank=False, unique=True)
    taxCodeDescription = model.CharField(max_length=50, null=False, blank=False)
    taxCodePercentage = models.DecimalField(max_digits=2, decimal_places=2, blank=False, null=False, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('taxCode',)

    def __str__(self):
        return f'{self.taxCode}, {self.taxCodeDescription}, {self.taxCodePercentage}'

    def create(self, ):
        return self.save()
    
    def change(self, taxCodeDescription, taxCodePercentage):
        self.taxCodeDescription = taxCodeDescription
        self.taxCodePercentage = taxCodePercentage
        return self.save()

class GLAccountGroup(models.Model):
    chartOfAccounts = models.ForeignKey(ChartOfaccounts, related_name='glAccountGroup', on_delete=PROTECT)
    accountGroup = models.CharField(max_length=4, null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    fromAccount = models.IntegerField(max_length=6, null=False, blank=False, unique=True)
    toAccount = models.IntegerField(max_length=6, null=False, blank=False, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('chartOfAccounts',)

    def __str__(self):
        return f'{self.chartOfAccounts}, {self.description}'

    def create(self, ):
        return self.save()
    
    def change(self, chartOfAccounts, description, fromAccount,  toAccount):
        self.chartOfAccounts = chartOfAccounts
        self.description = description
        self.fromAccount = fromAccount
        self.toAccount = toAccount
        return self.save()

class GeneralLedgeAccountMaster(models.Model):
    accountNumber = models.IntegerField(max_length=6, null=False, blank=False, unique=True)
    companyCode = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, unique=True, related_name='GeneralLedgeAccountMaster')
    glAccountGroup = models.ForeignKey(GLAccountGroup, max_length=4, null= False, blank=True, unique=True, related_name='GeneralLedgeAccountMaster')
    profitAndLossAccount = models.BooleanField()
    balanceSheetAccount = models.BooleanField()
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=135)
    accountCurrency = models.CharField(choices=CURRENCY, null=False, blank=False)
    balancesLocalCurrency = models.BooleanField()
    exchangeRateDiffKey = models.CharField(max_length=3)
    taxCategory = models.CharField(max_length=2)
    taxableItem = models.BooleanField()
    reconciliationAccountType = models.CharField(choices=RECONACCOUNT, null=False, blank=False)
    openItemMgt = models.BooleanField()
    lineItemDisplay = models.BooleanField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('accNum',)

    def __str__(self):
        return f'{self.accNum}, {self.shortDescription}'

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







