
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import GeneralLedgerAccountMaster, TaxCode, GeneralLedgerAccountGroup
from users.serializers import serializers
from datetime import datetime



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
    owner = serializers.ReadOnlyField(source='owner.username')
    # lastDateOfInterestCalculation = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d", input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"])
    # keyDateofLastInterest = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d", input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"])

    # def validate(self, value):
    #     return value.strftime('%Y-%m-%d') if value else value

    class Meta:
        model = GeneralLedgerAccountMaster
        # fields = (
        #     'url', 'owner', 'id', 'accountNumber', 'companyCode', 'glAccountGroup','profitAndLossAccount', 'balanceSheetAccount', 'shortDescription', 'longDescription', 'accountCurrency', 'balancesLocalCurrency',
        #     'exchangeRateDiffKey', 'taxCategory', 'taxableItem', 'reconciliationAccountType', 'openItemMgt', 'lineItemDisplay', 'dateCreated', 'dateChanged'
        #     )
        fields = '__all__'
