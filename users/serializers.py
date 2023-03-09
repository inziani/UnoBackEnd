
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import User, UserProfile, EmployeeIDInformation, EmployeeBankInformation, EmployeeDependants, EmployeeMaritalInformation, EmployeeNextOfKin
from activitys.models import ActivityCategory, Activity



class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    profile_pic = Base64ImageField(max_length=None, use_url=True,)

    class Meta:
        model = UserProfile
        fields = (
            'url', 
            'user', 
            'education_bio', 
            'professional_bio', 
            'professional_hobbies', 
            'personal_hobbies', 
            'social_hobbies', 
            'profile_pic', 
            'create_at', 
            'updated_at'
            )

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

