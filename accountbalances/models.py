from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model

from company.models import CompanyCode
from masterdata.models import GeneralLedgeAccountMaster
from company.constants import CURRENCY

# Create your models here.


class GLAccountBalances(models.Model):
    currentDate = models.DateField(auto_now_add=True)
    localCurrency = models.CharField(choices=CURRENCY, blank=False, null=False, max_length=3)
    companyCode  = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, related_name='companyCode_GLAccountBalances', on_delete=PROTECT)
    fiscalYear = models.IntegerField(null=False, blank=False)
    ledger = models.CharField(max_length=2, null=False, blank=False, unique=True)
    postingPeriod = models.IntegerField(null=False, blank=False, unique=True)
    accountNumber = models.ForeignKey(GeneralLedgeAccountMaster, max_length=6, null=False, blank=False, related_name='accountNumber_GLAccountBalances', on_delete=PROTECT)
    glLongDescription = models.ForeignKey(GeneralLedgeAccountMaster, max_length=135, related_name='glLongDescription_GLAccountBalances', on_delete=PROTECT)
    currency = models.CharField(max_length=3, null=False, blank=False)
    openingBalance = models.DecimalField(decimal_places=2, max_digits=15)
    periodDebit = models.DecimalField(decimal_places=2, max_digits=15)
    periodCredit = models.DecimalField(decimal_places=2, max_digits=15)
    closingBalance = models.DecimalField(decimal_places=2, max_digits=15)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('accountNumber', )

    def __str__(self):
        return f'{self.companyCode}, {self.accountNumber}, {self.glLongDescription}'

    def create(self, ):
        return self.save()
    
    def change(self, localCurrency, companyCode, fiscalYear, ledger, postingPeriod, 
    accountNumber, glLongDescription ,currency, openingBalance, periodDebit, periodCredit, 
    closingBalance):
        self.localCurrency = localCurrency
        self.companyCode = companyCode
        self.fiscalYear = fiscalYear
        self.ledger = ledger
        self.postingPeriod = postingPeriod
        self.accountNumber = accountNumber
        self.glLongDescription = glLongDescription
        self.currency = currency
        self.openingBalance = openingBalance
        self.periodDebit = periodDebit
        self.periodCredit = periodCredit
        self.closingBalance = closingBalance
        return self.save()

