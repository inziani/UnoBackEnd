from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model
# from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal

from company.constants import CURRENCY
from company.models import ChartOfAccounts, CompanyCode, ControllingArea, ReportingArea, BusinessArea
from .constants import RECONACCOUNT, ACCOUNTTYPE, FINANCIALSTATEMENT

# Create your models here.

class TaxCode(models.Model):
    taxCode = models.CharField(max_length=2, null=False, blank=False, unique=True)
    taxCodeDescription = models.CharField(max_length=50, null=False, blank=False)
    taxCodePercentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'), blank=False, null=False, unique=True)
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

class GeneralLedgerAccountGroup(models.Model):
    accountGroup = models.CharField(max_length=4, null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('accountGroup',)

    def __str__(self):
        return f'{self.accountGroup}, {self.description}'

    def create(self, ):
        return self.save()
    
    def change(self, description):
        self.description = description
        return self.save()

class GeneralLedgerAccountMaster(models.Model):
    accountNumber = models.IntegerField(null=False, blank=False, unique=True)
    companyCode = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, related_name='GeneralLedgerAccountMaster', on_delete=PROTECT)
    chartOfAccounts = models.ForeignKey(ChartOfAccounts, null=False, blank=False, related_name='GeneralLedgerAccountMaster', on_delete=PROTECT)
    accountGroup = models.CharField(null=False, blank=True, max_length=4)
    accountType = models.CharField(choices=ACCOUNTTYPE, null=False, blank=True, max_length=30)
    reconciliationAccountInput = models.BooleanField(null=False, blank=True)
    reconciliationAccountType = models.CharField(choices=RECONACCOUNT, null=False, blank=True, max_length=30)
    alternativeGLAccount = models.IntegerField(null=True, blank=True, unique=False)
    accountManagedinExternalSystem = models.BooleanField(null=True, blank=True)
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=135)
    financialStatementAccount = models.CharField(choices=FINANCIALSTATEMENT, null=False, blank=False, default='Balance Sheet Account', max_length=30)
    accountCurrency = models.CharField(choices=CURRENCY, null=False, blank=False, max_length=3)
    balancesInLocalCurrency = models.BooleanField(null=False, blank=True)
    exchangeRateKey = models.CharField(max_length=3, null=False, blank=True)
    taxCategory = models.CharField(max_length=2, null=False, blank=True)
    postingWithoutTaxAllowed = models.BooleanField(null=False, blank=True)
    openItemManagement = models.BooleanField(null=True, blank=True)
    lineItemManagement = models.BooleanField(null=False, blank=True)
    blockedForPosting = models.BooleanField(null=False, blank=True)
    markedForDeletion = models.BooleanField(null=False, blank=True)
    groupAccountNumber = models.IntegerField(null=False, blank=True, unique=False, default=0)
    tradingPartner = models.IntegerField(null=False, blank=True, unique=False, default=None)
    sortKey = models.CharField(null=False, blank=True, max_length=2)
    authorizationGroup = models.CharField(null=False, blank=True, max_length=4)
    fieldStatusGroup = models.CharField(null=False, blank=True, max_length=4)
    postAutomaticallyOnly = models.BooleanField(null=False, blank=True)
    relevantToCashFlow = models.BooleanField(null=False, blank=True)
    houseBank = models.CharField(null=False, blank=True, max_length=4)
    houseBankAccountID = models.IntegerField(null=False, blank=True, unique=False, default=0)
    controllingArea = models.ForeignKey(ControllingArea, max_length=4, null=False, blank=True, related_name='GeneralLedgerAccountMaster', on_delete=PROTECT)
    costElement = models.IntegerField(null=False, blank=True, unique=False, default=0)
    unitOfMeasure = models.CharField(null=False, blank=True, max_length=5)
    businessArea = models.ForeignKey(BusinessArea, max_length=4, null=False, blank=True, related_name='GeneralLedgerAccountMaster', on_delete=PROTECT)
    valuationGroup = models.CharField(null=False, blank=True, max_length=5)
    inflationKey = models.CharField(null=False, blank=True, max_length=2)
    toleranceGroup = models.CharField(null=False, blank=True, max_length=5)
    planningLevel = models.CharField(null=False, blank=True, max_length=2)
    supplementAutomaticPostings = models.BooleanField(null=False, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    try:
        tradingPartner = models.IntegerField(null=False, blank=True, unique=False, default=None)
    #    val = int(foo)
    except ValueError:
    # foo is something that cannot be converted to
    # a number. It could be an empty string, or a
    # string like 'hello'
    # provide a default value
        tradingPartner = None
    

    class Meta:
        ordering = ('accountNumber',)

    def __str__(self):
        return f'{self.companyCode}, {self.accountNumber}, {self.shortDescription}'

    def create(self, ):
        return self.save()
    
    def change(self,
    companyCode, accountGroup, profitAndLossAccount, balanceSheetAccount, shortDescription, 
        longDescription, accountCurrency, balancesLocalCurrency, exchangeRateDiffKey , taxCategory , reconciliationAccountType, toleranceGroup,  businessArea, costElement, controllingArea, houseBankAccountID, houseBank, relevantToCashFlow, postAutomaticallyOnly, fieldStatusGroup, authorizationGroup, sortKey, tradingPartner, groupAccountNumber, markedForDeletion, blockedForPosting, lineItemManagement, openItemManagement, postingWithoutTaxAllowed, exchangeRateKey, balancesInLocalCurrency , unitOfMeasure,planningLevel, accountManagedinExternalSystem, supplementAutomaticPostings, inflationKey, valuationGroup

        # keyDateofLastInterest, lastDateOfInterestCalculation, interestCalculationFrequency, interestIndicator
    
    ):
        self.companyCode = companyCode
        self.accountGroup = accountGroup
        self.profitAndLossAccount = profitAndLossAccount
        self.balanceSheetAccount = balanceSheetAccount
        self.shortDescription = shortDescription
        self.longDescription = longDescription
        self.accountCurrency = accountCurrency
        self.balancesLocalCurrency = balancesLocalCurrency
        self.exchangeRateDiffKey = exchangeRateDiffKey
        self.taxCategory = taxCategory
        self.reconciliationAccountType = reconciliationAccountType
        self.openItemManagement = openItemManagement
        return self.save()

   

       







