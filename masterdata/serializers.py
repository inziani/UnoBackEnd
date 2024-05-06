
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

class GeneralLedgerAccountMasterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = GeneralLedgerAccountMaster
        fields = '__all__'
