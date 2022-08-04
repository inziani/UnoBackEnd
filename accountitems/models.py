from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model

from company.models import CompanyCode
from masterdata.models import GeneralLedgerAccountMaster, TaxCode
from company.constants import CURRENCY
from .constants import POSTINGKEY

# Create your models here.

class GLDocument(models.Model):
    documentNumber = models.IntegerField(null=False, blank=False, unique=True)
    documentDate = models.DateField()
    postingDate = models.DateField()
    reference = models.CharField(max_length=50, null=False, blank=False)
    headerText = models.CharField(max_length=50, null=False, blank=False)
    companyCode = models.ForeignKey(CompanyCode, max_length=4, null=False, blank=False, related_name='companyCode_GLDocument', on_delete=PROTECT)
    accountNumber = models.ForeignKey(GeneralLedgerAccountMaster, max_length=6, null=False, blank=False, related_name='accountNumber_GLDocument', on_delete=PROTECT)
    shortDescription = models.CharField(max_length=50, null=False, blank=False)
    dr = models.CharField(choices=POSTINGKEY, max_length=6)
    cr = models.CharField(choices=POSTINGKEY, max_length=6)
    currency = models.CharField(choices=CURRENCY, max_length=35)
    amountInDocumentCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    taxCode = models.ForeignKey(TaxCode, max_length=2, null=False, blank=False, related_name='taxCode_GLDocument', on_delete=PROTECT)
    taxAmountInDocumentCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('accountNumber', )

    def __str__(self):
        return f'{self.companyCode}, {self.accountNumber}, {self.documentNumber}, {self.glLongDescription}'
    

class GLAccountLineItems(models.Model):
    accountNumber = models.ForeignKey(GeneralLedgerAccountMaster, max_length=6, null=False, blank=False,  related_name='accountNumber_GLAccountLineItems', on_delete=PROTECT)
    companyCode = models.ForeignKey(CompanyCode, on_delete=PROTECT, null=False, blank=False, related_name='companyCode_GLAccountLineItems')
    documentNumber = models.IntegerField(null=False, blank=False, unique=True)
    documentType = models.CharField(max_length=2, blank=False, null=False)
    documentDate = models.DateField(null=False, blank=False)
    localCurrency = models.CharField(max_length=3, null=False, blank=False, choices=CURRENCY)
    amountInLocalCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    taxCode = models.CharField(max_length=2, null=False, blank=False)
    taxAmountLocalCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    amountInForeignCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    taxAmountForeignCurrency = models.DecimalField(decimal_places=2, max_digits=17)
    clearingDocument = models.CharField(max_length=10)
    documentText = models.CharField(max_length=135, null=False, blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.companyCode}, {self.accountNumber}, {self.documentNumber}, {self.documentText}'

    def create(self, ):
        return self.save()
    
    def change(self, documentText):
        self.documentText = documentText
        return self.save()

