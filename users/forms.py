from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import models

from .models import User, UserProfile 

class RegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'first_name','last_name', 'phone_number', 'username', 'password', 'date_of_birth', 'gender', 'city', 'country')

  def save(self, commit=True):
    # Save the password in a hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    if commit:
      user.save()
    return user

class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'first_name','last_name', 'phone_number', 'username', 'password', 'date_of_birth', 'gender', 'city', 'country')
  
  def clean_password2(self):
    #Check that the two passwords match
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
       raise forms.ValidationError('The two passwords do not match')
    return password2

  def save(self, commit=True):
    #Save the provided password in a hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

class UserChangeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()
  
  class Meta:
    model = User
    fields = ('email', 'first_name','last_name', 'phone_number', 'username', 'password', 'date_of_birth', 'gender', 'city', 'country')

  def clean_password(self):
    # Regardless of what the user provides, return the initial value.
    # This is done here, rather than on the field, because the
    # field does not have access to the initial value
    return self.initial['password']




