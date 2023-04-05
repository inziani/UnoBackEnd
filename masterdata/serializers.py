
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import GeneralLedgerAccountMaster, TaxCode, GeneralLedgerAccountGroup
from users.serializers import serializers



class TaxCodeSerializer(HyperlinkedModelSerializer):
   
    class Meta:
        model = TaxCode
        fields = (
            'url', 'id', 'taxCode', 'taxCodeDescription', 'taxCodePercentage', 'dateCreated', 'dateChanged'
                )


class GeneralLedgerAccountGroupSerializer(ModelSerializer):

    class Meta:
        model = GeneralLedgerAccountGroup
        fields =  (
            'url', 'id', 'accountGroup', 'description', 
            'dateCreated', 'dateChanged' )

class GeneralLedgerAccountMasterSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GeneralLedgerAccountMaster
        # fields = (
        #     'url', 'owner', 'id', 'accountNumber', 'companyCode', 'glAccountGroup','profitAndLossAccount', 'balanceSheetAccount', 'shortDescription', 'longDescription', 'accountCurrency', 'balancesLocalCurrency',
        #     'exchangeRateDiffKey', 'taxCategory', 'taxableItem', 'reconciliationAccountType', 'openItemMgt', 'lineItemDisplay', 'dateCreated', 'dateChanged'
        #     )
        fields = '__all__'
