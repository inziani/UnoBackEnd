
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import TaxCode, GLAccountGroup, GeneralLedgeAccountMaster



class TaxCodeSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TaxCode
        fields = (
            'url', 'id', 'companyCode', 'taxCode', 'taxCodeDescription', 'taxCodePercentage', 'dateCreated', 'dateChanged', 'owner'
                )


class GLAccountGroupSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = GLAccountGroup
        fields =  (
            'url', 'owner', 'id', 'companyCode', 'chartOfAccounts', 'accountGroup', 'description', 'fromAccount' 
            'toAccount', 'dateCreated', 'dateChanged' )

class GeneralLedgeAccountMasterSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(source='activity_category', read_only=True)

    class Meta:
        model = GeneralLedgeAccountMaster
        fields = (
            'url', 'owner', 'id', 'accountNumber', 'companyCode', 'glAccountGroup','profitAndLossAccount', 'balanceSheetAccount', 'shortDescription', 'longDescription', 'accountCurrency', 'balancesLocalCurrency',
            'exchangeRateDiffKey', 'taxCategory', 'taxableItem', 'reconciliationAccountType', 'openItemMgt', 'lineItemDisplay', 'dateCreated', 'dateChanged'
            )
