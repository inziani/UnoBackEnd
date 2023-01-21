# Create your models here.

import rest_framework_simplejwt as jwt
from django.conf import settings
from datetime import datetime, timedelta
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .constants import GENDER

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(unique=True, max_length=255, default='USERNAME')
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=150)
  middle_name = models.CharField(max_length=150, default='middle')
  last_name = models.CharField(max_length=150)
  phone_number = models.CharField(max_length=13)
  date_of_birth = models.DateField(blank=True, null=True)
  gender = models.CharField(choices=GENDER, default='',max_length=6)
  city = models.CharField(verbose_name= _("City"), blank=True, null=True, max_length=255)
  country = models.CharField(verbose_name= _("Country"), blank=True, null=True, max_length=255)
  is_active = models.BooleanField(default=True)
  # The is_active flag offers users a chance to deactivate their account as opposed to deletion which completely removes a users account from the application.
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  # The is_staff flag is expected by django to determine who can and cannot log on to the admin site. The flag will be active for staff only
  date_joined = models.DateTimeField(default=timezone.now)

  objects = UserManager() 

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'username','phone_number' ]

  class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'

  def display_name(self):
    return f'{self.first_name} {self.middle_name} {self.last_name}'

  def __str__(self):
    """ Returns the string representation os this 'User'. This string is used when a 'User' is printed in the console"""
    return f'{self.first_name} {self.middle_name} {self.last_name}'

  def email_user(self,subject, message, from_email = None, **kwargs):
    "Sends and email to this user"
    send_mail( subject, message, from_email, [self.email], **kwargs)


  @property
  def tokenJwT(self):
    " Generate token using user.token instead of user.generate_jwt_token"
    return self.generate_jwt_token()

  def generate_jwt_token(self):
    """
    Generates a JSON web token that stores he user's ID and has an expiry date set to 60 days into the future
    """

    dt = datetime.now() + timedelta(days=60)

    token = jwt.encode({
      'id': self.pk,
      'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm="HS256")
    return token.decode('utf-8')

class UserProfile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
  education_bio = models.CharField(max_length=255, blank=True, null=True)
  professional_bio = models.CharField(max_length=255, blank=True, null=True)
  professional_hobbies = models.CharField(max_length=255, blank=True, null=True)
  personal_hobbies = models.CharField(max_length=255, blank=True, null=True)
  social_hobbies = models.CharField(max_length=255, blank=True, null=True)
  profile_pic = models.ImageField(null=True)
  is_verified = models.BooleanField(default=False)
  create_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{ self.user.first_name } { self.user.middle_name } { self.user.last_name }'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


class EmployeeIDInformation(models.Model):
  staffID = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="emp_id")
  identificationDocument = models.CharField(max_length=150)
  identificationNumber = models.CharField(max_length=150)
  taxNumber = models.CharField(max_length=150)
  startDate= models.DateTimeField(default=timezone.now)
  endDate = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return f'{self.staffID.id}  - { self.staffID.first_name } { self.staffID.middle_name } { self.staffID.last_name }' 
    

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

class EmployeeNextOfKin(models.Model):
  staffID = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="emp_kin")
  first_name = models.CharField(max_length=150)
  middle_name = models.CharField(max_length=150, default='Middle')
  last_name = models.CharField(max_length=150)
  email = models.EmailField(unique=False)
  relationship = models.CharField(max_length=150)
  phone_number = models.CharField(max_length=13)
  date_of_birth = models.DateField(blank=True, null=True)
  gender = models.CharField(choices=GENDER, default='',max_length=6)
  city = models.CharField(verbose_name= _("City"), blank=True, null=True, max_length=255)
  country = models.CharField(verbose_name= _("Country"), blank=True, null=True, max_length=255)
  residentialAddress = models.CharField(max_length=150)
  identificationDocument = models.CharField(max_length=150)
  identificationNumber = models.CharField(max_length=150)
  taxNumber = models.CharField(max_length=150)
  

  def __str__(self):
    return f'{ self.staffID.id}  - { self.staffID.first_name } { self.staffID.middle_name } { self.staffID.last_name }' 
    

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

class EmployeeMaritalInformation(models.Model):
  staffID = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="emp_marital")
  first_name = models.CharField(max_length=150)
  middle_name = models.CharField(max_length=150, default='Middle')
  last_name = models.CharField(max_length=150)
  email = models.EmailField(unique=False)
  phone_number = models.CharField(max_length=13)
  date_of_birth = models.DateField(blank=True, null=True)
  relationship = models.CharField(max_length=150)
  marriageDate = models.DateField(blank=True, null=True)
  marriageCertificateNumber = models.CharField(max_length=150)
  gender = models.CharField(choices=GENDER, default='',max_length=6)
  identificationDocument = models.CharField(max_length=150)
  identificationNumber = models.CharField(max_length=150)
  taxNumber = models.CharField(max_length=150)
  residentialAddress = models.CharField(max_length=150)
  city = models.CharField(verbose_name= _("City"), blank=True, null=True, max_length=255)
  country = models.CharField(verbose_name= _("Country"), blank=True, null=True, max_length=255)
  
  
  

  def __str__(self):
    return f'{ self.staffID.id}  - { self.staffID.first_name } { self.staffID.middle_name } { self.staffID.last_name }' 
   

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

class EmployeeDependants(models.Model):
  staffID = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="emp_dependants")
  email = models.EmailField(unique=False)
  first_name = models.CharField(max_length=150)
  middle_name = models.CharField(max_length=150, default='Middle')
  last_name = models.CharField(max_length=150)
  phone_number = models.CharField(max_length=13)
  date_of_birth = models.DateField(blank=True, null=True)
  gender = models.CharField(choices=GENDER, default='',max_length=6)
  city = models.CharField(verbose_name= _("City"), blank=True, null=True, max_length=255)
  country = models.CharField(verbose_name= _("Country"), blank=True, null=True, max_length=255)
  relationship = models.CharField(max_length=150)
  residentialAddress = models.CharField(max_length=150)
  identificationDocument = models.CharField(max_length=150)
  identificationNumber = models.CharField(max_length=150)
  taxNumber = models.CharField(max_length=150)
  

  def __str__(self):
    return f'{ self.staffID.id}  - { self.staffID.first_name } { self.staffID.middle_name } { self.staffID.last_name }' 
   

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

class EmployeeBankInformation(models.Model):
  staffID = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="emp_bank")
  bank = models.CharField(max_length=150)
  bankBranch = models.CharField(max_length=150)
  bankAccountNumber = models.CharField(max_length=150)
  city = models.CharField(max_length=150)
  country = models.CharField(max_length=150)

  def __str__(self):
    return f'{ self.staffID.id}  - { self.staffID.first_name } { self.staffID.middle_name } { self.staffID.last_name }' 
   

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)









