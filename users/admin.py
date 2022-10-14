from django.contrib import admin
from django.contrib.auth import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager
# Register your models here.

from .models import User, UserProfile, EmployeeIDInformation, EmployeeNextOfKin, EmployeeMaritalInformation, EmployeeDependants, EmployeeBankInformation
from .forms import UserCreationForm, UserChangeForm, RegistrationForm

employeeModels = [EmployeeIDInformation, EmployeeNextOfKin, EmployeeMaritalInformation, EmployeeDependants, EmployeeBankInformation]

class EmployeeBankInformationInline(admin.StackedInline):
    model = EmployeeBankInformation
    can_delete = False
    verbose_plural_name ="Employee Bank Information"
    foreignkey_name = 'staffID'

class EmployeeDependantsInline(admin.StackedInline):
    model = EmployeeDependants
    can_delete = False
    verbose_plural_name ="Employee Dependants Information"
    foreignkey_name = 'staffID'

class EmployeeMaritalInformationInline(admin.StackedInline):
    model = EmployeeMaritalInformation
    can_delete = False
    verbose_plural_name ="Employee Marital Information"
    foreignkey_name = 'staffID'

class EmployeeNextOfKinInline(admin.StackedInline):
    model = EmployeeNextOfKin
    can_delete = False
    verbose_plural_name ="Employee Next of Kin Information"
    foreignkey_name = 'staffID'

class EmployeeIDInformationInline(admin.StackedInline):
    model = EmployeeIDInformation
    can_delete = False
    verbose_plural_name ="Employee ID Information"
    foreignkey_name = 'staffID'

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_plural_name ="User Profile"
    foreignkey_name = 'user'

class CustomUserAdmin(UserAdmin):
  model = User
  form = UserChangeForm
  add_form = UserCreationForm

  list_display = ('email', 'first_name', 'last_name', 'username', 'phone_number', 'is_staff', 'is_superuser', 'date_of_birth')
  # inlines = (EmployeeIDInformationInline,)
  inlines = (UserProfileInline, EmployeeIDInformationInline, EmployeeNextOfKinInline, EmployeeMaritalInformationInline, 
  EmployeeDependantsInline, EmployeeBankInformationInline,)
  list_filter = ['is_superuser']

  add_fieldsets = UserAdmin.add_fieldsets + (
    ('Personal Information',
    {'fields':(
      'email',
      ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender')
      , 'phone_number', 'city','country',)
      }),
    ('Company Information',{
      'fields':(
        'is_staff', 'is_superuser','is_active',
      )
    }),
  )

  fieldsets = UserAdmin.fieldsets + (
  ('Personal Information', 
  {'fields':(
    'gender', 'city','country','date_of_birth',
    )
    }),
  )

  search_fields = ('email', 'phone_number')
  ordering = ['email']
  filter_horizontal = ()

  def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)

