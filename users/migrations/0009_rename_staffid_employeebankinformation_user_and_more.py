# Generated by Django 4.0.3 on 2022-10-15 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_employeedependants_middle_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeebankinformation',
            old_name='staffID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='employeedependants',
            old_name='staffID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='employeeidinformation',
            old_name='staffID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='employeemaritalinformation',
            old_name='staffID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='employeenextofkin',
            old_name='staffID',
            new_name='user',
        ),
    ]