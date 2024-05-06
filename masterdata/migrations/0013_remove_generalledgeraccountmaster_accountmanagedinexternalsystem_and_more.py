# Generated by Django 4.0.3 on 2024-02-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0012_remove_generalledgeraccountmaster_interestcalculationfrequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='accountManagedinExternalSystem',
        ),
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='inflationKey',
        ),
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='planningLevel',
        ),
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='supplementAutomaticPostings',
        ),
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='unitOfMeasure',
        ),
        migrations.RemoveField(
            model_name='generalledgeraccountmaster',
            name='valuationGroup',
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='alternativeGLAccount',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='costElement',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='groupAccountNumber',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='houseBankAccountID',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='tradingPartner',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
