
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Company, CompanyCode, ChartOfaccounts, ReportingArea
from users.serializers import serializers



class CompanySerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Company
        fields = (
            'url', 'id', 'company', 'companyName', 'street', 'postOfficeBox', 'postalCode', 'country', 'language',
            'currency', 'landLine', 'mobileNumber', 'email', 'dateCreated', 'dateChanged', 'owner')


class CompanyCodeSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = CompanyCode
        # fields = '__all__'
        fields =  ('url', 'owner', 'id', 'code', 'description', 'company', 'dateCreated', 'dateChanged')

class ChartOfaccountsSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(source='activity_category', read_only=True)
     owner = serializers.ReadOnlyField(source='owner.username')


     class Meta:
        model = ChartOfaccounts
        fields = (
                 'url', 'owner', 'id', 'coaCode', 'companyCode',  'description', 'language', 'lengthGlAccNumber',
                'status', 'dateCreated', 'dateChanged'
                 )

class ReportingAreaSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(source='activity_category', read_only=True)
     owner = serializers.ReadOnlyField(source='owner.username')

     class Meta:
        model = ReportingArea
        fields = ('url', 'owner', 'id')
