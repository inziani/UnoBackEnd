from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model
# from django_countries.fields import CountryField


from .constants import LANGUAGE, CURRENCY


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
    landLine = models.IntegerField(null=True, blank=True)
    mobileNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

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
    code = models.IntegerField(null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='companyCode', on_delete=PROTECT)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return f'{self.code}, {self.description}'

    def create(self, ):
        return self.save()
    
    def change(self, description, company ):
        self.description = description
        self.company = company
        return self.save()

class ChartOfAccounts(models.Model):
    coaCode = models.CharField(max_length=4, null=False, blank=False, unique=True)
    companyCode = models.ForeignKey(CompanyCode, related_name='companyCode_ChartOfaccounts', on_delete=PROTECT)
    description = models.CharField(max_length=50, null=False, blank=False)
    language = models.CharField(choices=LANGUAGE, default='en', max_length=35)
    lengthAccNumber = models.IntegerField()
    status = models.BooleanField(null=False, default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('coaCode',)

    def __str__(self):
        return f'{self.companyCode}, {self.coaCode}, {self.description}'

    def create(self, ):
        return self.save()

    def change(self, coaCode, description, language, lengthGlAccNumber, status):
        self.coaCode = coaCode
        self.description = description
        self.language = language
        self.lengthGlAccNumber = lengthGlAccNumber
        self.status = status
        self.language = language
        return self.save()
    

class ReportingArea(models.Model):
    pass

