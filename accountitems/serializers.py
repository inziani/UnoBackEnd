from rest_framework.serializers import HyperlinkedModelSerializer

from .models import GLDocument, GLAccountLineItems, 

class GLDocumentSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = GLDocument
        fields = (
            'url', 'id', 'documentNumber', 'documentDate', 'postingDate',  'reference', 'headerText', 'companyCode',
            'accountNumber', 'shortDescription', 'dr', 'cr', 'currency', 'amountInDocumentCurrency', 'taxCode', 'taxAmountInDocumentCurrency', 'dateCreated', 'dateChanged', 'owner'
        )

class GLAccountLineItemsSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = GLAccountLineItems
        fields = ( 'url', 'id', 'accountNumber', 'companyCode', 'documentNumber', 'documentType', 'documentDate',
        'localCurrency', 'amountInLocalCurrency', 'taxCode', 'taxAmountLocalCurrency', 'amountInForeignCurrency',
        'taxAmountForeignCurrency', 'clearingDocument', 'documentText', 'dateCreated', 'dateChanged', 'owner'
        )
