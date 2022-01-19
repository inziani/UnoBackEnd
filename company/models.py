from django.db import models
from django_countries.fields import CountryField


from constants import LANGUAGE, CURRENCY

# Create your models here.


class Company(models.Model):
    company = models.CharField(max_length=4, null=False, blank=False, unique=True)
    companyName = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postOfficeBox = models.IntegerField(null=True, default=12345, max_length=5, blank=False)
    postalCode = models.IntegerField(null=True, default=00100, max_length=4, blank=False)
    country = CountryField()
    language = models.CharField(choices=LANGUAGE, default='', max_length=2)
    currency = models.CharField(choices=CURRENCY, default=KSH, max_length=3)
    landLine = models.IntegerField(max_length=15, null=True, blank=True)
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

class ChartOfaccounts(model.models):
    pass


class CompanyCode(models.Model):
    code = models.IntegerField(max_length=4, null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='company', on_delete=PROTECT)
    coa = models.
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

class ControllingArea(models.Model):
    pass



