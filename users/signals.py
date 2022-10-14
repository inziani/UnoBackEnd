from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile, EmployeeIDInformation, EmployeeNextOfKin, EmployeeMaritalInformation, EmployeeDependants, EmployeeBankInformation 


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
  if created:
    user_profile = UserProfile.objects.create(user = instance)
  instance.user_profile.save()


@receiver(post_save, sender=User)
def createEmpID(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    emp_id = EmployeeIDInformation.objects.create(staffID = instance)
  instance.emp_id.save()

@receiver(post_save, sender=User)
def createEmpKin(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    emp_kin = EmployeeNextOfKin.objects.create(staffID = instance)
  instance.emp_kin.save()

@receiver(post_save, sender=User)
def createEmpMarital(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    emp_marital = EmployeeMaritalInformation.objects.create(staffID = instance)
  instance.emp_marital.save()

@receiver(post_save, sender=User)
def createEmpDependants(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    emp_dependants = EmployeeDependants.objects.create(staffID = instance)
  instance.emp_dependants.save()

@receiver(post_save, sender=User)
def createEmpBank(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    emp_bank = EmployeeBankInformation.objects.create(staffID = instance)
  instance.emp_bank.save()

