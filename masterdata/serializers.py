
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import GeneralLedgerAccountMaster, TaxCode, GeneralLedgerAccountGroup
from company.models import Company, CompanyCode, ChartOfAccounts, ReportingArea, ControllingArea, BusinessArea
from users.serializers import serializers
from company.serializers import CompanySerializer, CompanyCodeSerializer, ChartOfAccountsSerializer, ControllingAreaSerializer, ReportingAreaSerializer, BusinessAreaSerializer
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

class GeneralLedgerAccountMasterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # companyCode = CompanyCodeSerializer()
    # chartOfAccounts = ChartOfAccountsSerializer()
    # controllingArea = ControllingAreaSerializer()
    # businessArea = BusinessAreaSerializer()


    class Meta:
        model = GeneralLedgerAccountMaster
        fields = '__all__'
        # fields = ('url', 'accountNumber', 'accountType', 'owner', 'companyCode', 'chartOfAccounts', 'controllingArea', 'businessArea')
