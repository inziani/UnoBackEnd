from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile, EmployeeIDInformation, EmployeeNextOfKin, EmployeeMaritalInformation, EmployeeDependants, EmployeeBankInformation 


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user = instance)

@receiver(post_save, sender=User)
def createEmpID(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    EmployeeIDInformation.objects.create(staffID = instance)
 
@receiver(post_save, sender=User)
def createEmpKin(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    EmployeeNextOfKin.objects.create(staffID = instance)
  
@receiver(post_save, sender=User)
def createEmpMarital(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    EmployeeMaritalInformation.objects.create(staffID = instance)

@receiver(post_save, sender=User)
def createEmpDependants(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    EmployeeDependants.objects.create(staffID = instance)

@receiver(post_save, sender=User)
def createEmpBank(sender, instance, created, **kwargs):
  if created and instance.is_staff == True:
    EmployeeBankInformation.objects.create(staffID = instance)
 

