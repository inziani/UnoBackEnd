from django.db import models

from masterdata import ChartOfaccounts

# Create your models here.

class GLAccountGroup(models.Model):
    chartOfAccounts = models.ForeignKey(ChartOfaccounts, related_name='glAccountGroup', on_delete=PROTECT)
    accountGroup = models.CharField(max_length=4, null=False, blank=False, unique=True)
    description = models.CharField(max_length=50, null=False, blank=False)
    fromAccount = models.IntegerField(max_length=6, null=False, blank=False)
    toAccount = models.IntegerField(max_length=6, null=False, blank=False)
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




