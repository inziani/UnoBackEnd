# Create your models here.

#import _typeshed
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .constants import GENDER

#from __future__import import unicode_literals


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
  country = CountryField(multiple=True,  blank_label='(select country)', default='')
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'username','phone_number' ]

  class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'

  def display_name(self):
    return f'{self.first_name} + " " {self.last_name}'

  def __str__(self):
        return self.email

  def email_user(self,subject, message, from_email = None, **kwargs):
    "Sends and email to this user"
    send_mail( subject, message, from_email, [self.email], **kwargs)
  

class UserProfile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
  bio = models.CharField(max_length=255, blank=True, null=True)
  hobbies = models.CharField(max_length=150, blank=True, null=True)
  profile_pic = models.ImageField()
  is_verified = models.BooleanField(default=False)
  create_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.user.email







