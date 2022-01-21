from django.db import models

from company import companyCode
from masterdata import GeneralLedgeAccountMaster, TaxCode
from company.constants import CURRENCY
from constants import POSTINGKEY

# Create your models here.

class GLDocument(models.Model):
    documentDate = models.DateField()
    postingDate = models.DateField()
    reference = models.CharField(max_length=50, null=False, blank=False)
    headerText = models.CharField(max_length=50, null=False, blank=False)
    companyCode = companyCode  = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, unique=True, related_name='GLDocument')
    accountNumber = models.ForeignKey(GeneralLedgeAccountMaster, max_length=6. null=False, blank=False, unique=True, related_name='GLDocument')
    shortDescription = models.CharField(max_length=50, null=False, blank=False)
    dr = models.CharField(choices=POSTINGKEY)
    cr = models.CharField(choices=POSTINGKEY)
    currency = models.CharField(choices=CURRENCY)
    amountInDocumentCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    taxCode = models.ForeignKey(TaxCode, max_length=2, null=False, blank=False, related_name='GLDocument')
    taxAmountInDocumentCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)
    


class GLAccountLineItems(models.Model):
    accountNumber = models.ForeignKey(GeneralLedgeAccountMaster, max_length=6. null=False, blank=False, unique=True), related_name='GLAccountLineItems'
    documentNumber = models.IntegerField(max_length=13, null=False, blank=False, unique=True)
    documentType = models.CharField(max_length=2, blank=False, null=False)
    documentDate = models.DateField(null=False, blank=False)
    localCurrency = models.CharField(max_length=3, null=False, blank=False, choices=CURRENCY)
    amountInLocalCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    taxCode = models.CharField(max_length=2, null=False, blank=False)
    taxAmountLocalCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    amountInForeignCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    taxAmountForeignCurrency = models.DecimalField(decimal_places=2, max_digits=None)
    clearingDocument = models.CharField()
    documentText = models.CharField(max_length=135, null=False, blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.accountNumber}'

    def create(self, ):
        return self.save()
    
    def change(self, documentText):
        self.documentText = documentText
        return self.save()

