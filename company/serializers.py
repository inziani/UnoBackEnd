
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Company, CompanyCode, ChartOfAccounts, ReportingArea, ControllingArea, BusinessArea
from users.serializers import serializers




class CompanySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = (
            'url', 'id', 'company', 'companyName', 'street', 'postOfficeBox', 'postalCode', 'country', 'language',
            'currency', 'landLine', 'mobileNumber', 'email', 'dateCreated', 'dateChanged')


class CompanyCodeSerializer(serializers.ModelSerializer):
    # company = serializers.StringRelatedField()

    class Meta:
        model = CompanyCode
        fields =  ('url', 'id', 'companyCode', 'companyCodeName', 'company', 'dateCreated', 'dateChanged')
        # fields = '__all__'

class ChartOfAccountsSerializer(serializers.ModelSerializer):
    # companyCode = serializers.StringRelatedField()

    class Meta:
        model = ChartOfAccounts
        fields = (
                 'url', 'id', 'coaCode', 'companyCode',  'chartOfAccountsName', 'language', 'lengthAccNumber',
                'blockedForPosting', 'dateCreated', 'dateChanged'
                 )

class ReportingAreaSerializer(serializers.ModelSerializer):
    companyCode = serializers.StringRelatedField()
    
    class Meta:
        model = ReportingArea
        fields = ('url', 'id', 'reportingArea', 'reportingAreaName', 'personResponsible', 'companyCode',
        'dateCreated', 'dateChanged')

class ControllingAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ControllingArea
        fields = ('url', 'id', 'controllingArea', 'controllingAreaName', 'personResponsible', 'companyCode', 'dateCreated', 'dateChanged')

class BusinessAreaSerializer(serializers.ModelSerializer):
    companyCode = serializers.StringRelatedField()

    class Meta:
        model = BusinessArea
        fields = ('url', 'id', 'businessArea', 'businessAreaName', 'personResponsible', 'companyCode', 'dateCreated', 'dateChanged')
