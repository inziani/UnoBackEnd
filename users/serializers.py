
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import User, UserProfile, EmployeeIDInformation, EmployeeBankInformation, EmployeeDependants, EmployeeMaritalInformation, EmployeeNextOfKin
from activitys.models import ActivityCategory, Activity

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['phone_number'] = user.phone_number
        token['date_of_birth'] = user.date_of_birth
        token['email'] = user.email
        token['gender'] = user.gender
        token['city'] = user.city
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        return token


class UserSerializer(HyperlinkedModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 12,
        write_only = True
    )
    

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'city', 'country', 'password', 'is_active','is_superuser', 'is_staff', 'date_joined')
        

    def create(self, validated_data):
        # Use the create_user method to create new user
        return User.objects.create_user(**validated_data)

class UserProfileSerializer(HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name = 'userprofile-detail', queryset=User.objects.all())

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'bio', 'hobbies', 'profile_pic', 'create_at', 'updated_at')

class EmployeeIDInformationSerializer(ModelSerializer):
    staffID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = EmployeeIDInformation
        fields = ('url', 'staffID', 'identificationDocument', 'identificationNumber', 'taxNumber', 'startDate', 'endDate')

class EmployeeNextOfKinSerializer(ModelSerializer):
    staffID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = EmployeeNextOfKin
        fields = ('staffID', 'email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'date_of_birth', 'relationship','gender', 'city', 'country', 'residentialAddress', 'identificationDocument', 'identificationNumber', 'taxNumber')

class EmployeeMaritalInformationSerializer(ModelSerializer):
    staffID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = EmployeeMaritalInformation
        fields = ('staffID', 'email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'date_of_birth', 'relationship', 'marriageDate', 'marriageCertificateNumber', 'gender', 'city', 'country', 'residentialAddress', 'identificationDocument', 'identificationNumber', 'taxNumber')

class EmployeeDependantsSerializer(ModelSerializer):
    staffID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = EmployeeDependants
        fields = ('staffID', 'email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'date_of_birth', 'relationship', 'gender', 'city', 'country', 'residentialAddress', 'identificationDocument', 'identificationNumber', 'taxNumber')

class EmployeeBankInformationSerializer(ModelSerializer):
    staffID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = EmployeeBankInformation
        fields = ('staffID', 'bank', 'bankBranch', 'bankAccountNumber', 'city', 'country')

class RegistrationSerializer(HyperlinkedModelSerializer):
    """ Serializer registration requests and creates new user"""
    password = serializers.CharField(
        max_length = 128,
        min_length = 12,
        write_only = True
    )
    # The client should not be able to send a token along with a registration request. Make the request readonly to handle it.
    token = serializers.CharField(max_length=255, read_only = True)

    class Meta:
        model = User
        # List all the fields that could possible be included in a request or response including fields specified explicitly above
        fields = ['id','first_name','last_name', 'date_of_birth','phone_number','username','email','gender', 'city', 'password','token']

    def create(self, validated_data):
        # Use the create_user method to create new user
        return User.objects.create_user(**validated_data)
