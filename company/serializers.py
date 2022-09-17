
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

    class Meta:
        model = CompanyCode
        fields =  ('url', 'id', 'companyCode', 'companyCodeName', 'company', 'dateCreated', 'dateChanged')

class ChartOfAccountsSerializer(serializers.ModelSerializer):

     class Meta:
        model = ChartOfAccounts
        fields = (
                 'url', 'id', 'coaCode', 'companyCode',  'chartOfAccountsName', 'language', 'lengthAccNumber',
                'status', 'dateCreated', 'dateChanged'
                 )

class ReportingAreaSerializer(serializers.ModelSerializer):

     class Meta:
        model = ReportingArea
        fields = ('url', 'id', 'reportingArea', 'reportingAreaName', 'personResponsible', 'chartOfAccounts', 'companyCode',
        'dateCreated', 'dateChanged')

class ControllingAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ControllingArea
        fields = ('url', 'id', 'controllingArea', 'controllingAreaName', 'personResponsible', 'chartOfAccounts', 'companyCode', 'dateCreated', 'dateChanged')

class BusinessAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessArea
        fields = ('url', 'id', 'businessArea', 'businessAreaName', 'personResponsible', 'chartOfAccounts', 'companyCode', 'dateCreated', 'dateChanged')
