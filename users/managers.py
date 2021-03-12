from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, password, username, phone_number, **extra_fields):

    "Create and save the user with the supplied email and password"
    
    if not email:
      raise ValueError('Email is a required field')
    username = username
    password = password
    phone_number = phone_number
    email = self.normalize_email(email)
    user = self.model(email = email, **extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self, email, password, username, phone_number, **extra_fields):
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, username, phone_number **extra_fields)

  def create_superuser(self, email, password, username=None, **extra_fields):
    username = username
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser = True.')
    if extra_fields.get('is_staff') is not True:
     raise ValueError('is_staff must have is_staff = True.')
    if extra_fields.get('is_active') is not True:
      raise ValueError('is_active must have is_active = True.')
    return self.create_user(email, password, username, **extra_fields)
