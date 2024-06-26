# Generated by Django 4.0.3 on 2024-03-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0020_alter_generalledgeraccountmaster_openitemmanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='accountManagedinExternalSystem',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='alternativeGLAccount',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
