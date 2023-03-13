
# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.timezone import now



from .constants import LANGUAGE, CURRENCY
from users.models import User


# Create your models here.

class Company(models.Model):
    company = models.CharField(max_length=4, null=False, blank=False, unique=True)
    companyName = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postOfficeBox = models.IntegerField(null=True, default=12345, blank=False)
    postalCode = models.IntegerField(null=True, default=100, blank=False)
    country = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(choices=LANGUAGE, default='en', max_length=35)
    currency = models.CharField(choices=CURRENCY, default='KSH', max_length=3)
    landLine = models.CharField(null=True, blank=True, max_length=12)
    mobileNumber = models.CharField(null=True, blank=True, max_length=12)
    email = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('company',)

    def __str__(self):
        return f'{self.company}, {self.companyName}'

    def create(self, ):
        return self.save()

    def change(self, companyName, street, postOfficeBox, postalCode, country, language, currency ):
        self.companyName = companyName
        self.street = street
        self.postOfficeBox = postOfficeBox
        self.postalCode = postalCode
        self.country = country
        self.language = language
        self.currency = currency
        return self.save()

class CompanyCode(models.Model):
    companyCode = models.IntegerField(null=False, blank=False, unique=True)
    companyCodeName = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='CompanyCode', on_delete=PROTECT)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('companyCode',)

    def __str__(self):
        return f'{self.companyCode}, {self.companyCodeName}'

    def create(self, ):
        return self.save()
    
    def change(self, companyCodeName, company ):
        self.companyCodeName = companyCodeName
        self.company = company
        return self.save()

class ChartOfAccounts(models.Model):
    coaCode = models.CharField(max_length=4, null=False, blank=False, unique=True)
    companyCode = models.ForeignKey(CompanyCode, related_name='ChartOfaccounts', on_delete=PROTECT)
    chartOfAccountsName = models.CharField(max_length=50, null=False, blank=False)
    language = models.CharField(choices=LANGUAGE, default='en', max_length=35)
    lengthAccNumber = models.IntegerField()
    blockedForPosting = models.BooleanField(null=False, default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('coaCode',)

    def __str__(self):
        return f'{self.coaCode}, {self.chartOfAccountsName}'

    def create(self, ):
        return self.save()

    def change(self, coaCode, chartOfAccountsName, language, lengthGlAccNumber, status):
        self.coaCode = coaCode
        self.chartOfAccountsName = chartOfAccountsName
        self.language = language
        self.lengthGlAccNumber = lengthGlAccNumber
        self.status = status
        self.language = language
        return self.save()
    

class ReportingArea(models.Model):
    reportingArea = models.CharField(max_length=4, null=False, blank=False, unique=True, default='')
    reportingAreaName = models.CharField(max_length=50, null=False, blank=False, default='')
    personResponsible = models.CharField(max_length=135, null=False, blank=False, default='')
    companyCode = models.ForeignKey(CompanyCode, related_name='ReportingArea', on_delete=PROTECT, default='')
    dateCreated = models.DateTimeField(default=now)
    dateChanged = models.DateTimeField(default=now)

    class Meta:
        ordering = ('reportingArea',)

    def __str__(self):
        return f'{self.reportingArea}, {self.reportingAreaName}'

    def create(self, ):
        return self.save()
    
    def change(self, reportingAreaName, companyCode ):
        self.reportingAreaName = reportingAreaName
        self.companyCode = companyCode
        return self.save()
    

class ControllingArea(models.Model):
    controllingArea = models.CharField(max_length=4, null=False, blank=False, unique=True,default='')
    controllingAreaName = models.CharField(max_length=50, null=False, blank=False, default='')
    personResponsible = models.CharField(max_length=135, null=False, blank=False, default='')
    companyCode = models.ForeignKey(CompanyCode, related_name='ControllingArea', on_delete=PROTECT, default='')
    dateCreated = models.DateTimeField(default=now)
    dateChanged = models.DateTimeField(default=now)

    class Meta:
        ordering = ('controllingArea',)

    def __str__(self):
        return f'{self.controllingArea}, {self.controllingAreaName}'

    def create(self, ):
        return self.save()
    
    def change(self, controllingAreaName, companyCode ):
        self.controllingAreaName = controllingAreaName
        self.companyCode = companyCode
        return self.save()
    

class BusinessArea(models.Model):
    businessArea = models.CharField(max_length=4, null=False, blank=False, unique=True, default='')
    businessAreaName = models.CharField(max_length=50, null=False, blank=False, default='')
    personResponsible = models.CharField(max_length=135, null=False, blank=False, default='')
    companyCode = models.ForeignKey(CompanyCode, related_name='BusinessArea', on_delete=PROTECT, default='')
    dateCreated = models.DateTimeField(default=now)
    dateChanged = models.DateTimeField(default=now)

    class Meta:
        ordering = ('businessArea',)

    def __str__(self):
        return f'{self.businessArea}, {self.businessAreaName}'

    def create(self, ):
        return self.save()
    
    def change(self, businessAreaName, companyCode ):
        self.businessAreaName = businessAreaName
        self.companyCode = companyCode
        return self.save()
    

