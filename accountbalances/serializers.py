from rest_framework.serializers import HyperlinkedModelSerializer

from .models import GLAccountBalances
from users.serializers import serializers



class GLAccountBalancesSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GLAccountBalances
        fields = (
            'url','id', 'currentDate', 'localCurrency',  'companyCode',  'fiscalYear', 'ledger', 'postingPeriod', 'accountNumber', 'glLongDescription', 'currency', 'openingBalance', 'periodDebit', 'periodCredit', 'closingBalance', 'dateCreated', 'dateChanged', 'owner')
            
