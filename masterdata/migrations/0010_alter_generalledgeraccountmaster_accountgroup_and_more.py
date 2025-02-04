# Generated by Django 4.0.3 on 2024-01-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_landline_alter_company_mobilenumber'),
        ('masterdata', '0009_generalledgeraccountgroup_taxcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='accountGroup',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='accountType',
            field=models.CharField(blank=True, choices=[('Assets', 'Assets'), ('Accounts Payables', 'Accounts Payable'), ('Accounts Receivables', 'Accounts Receivable'), ('Materials', 'Materials'), ('General Ledger', 'General Ledger')], max_length=30),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='alternativeGLAccount',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='authorizationGroup',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='businessArea',
            field=models.ForeignKey(blank=True, max_length=4, on_delete=django.db.models.deletion.PROTECT, related_name='GeneralLedgerAccountMaster', to='company.businessarea'),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='controllingArea',
            field=models.ForeignKey(blank=True, max_length=4, on_delete=django.db.models.deletion.PROTECT, related_name='GeneralLedgerAccountMaster', to='company.controllingarea'),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='costElement',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='fieldStatusGroup',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='groupAccountNumber',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='houseBank',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='houseBankAccountID',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='inflationKey',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='interestCalculationFrequency',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='planningLevel',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='reconciliationAccountType',
            field=models.CharField(blank=True, choices=[('Assets', 'Assets'), ('Accounts Payables', 'Accounts Payable'), ('Accounts Receivables', 'Accounts Receivable'), ('Materials', 'Materials'), ('Not Required', 'Not Required')], max_length=30),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='toleranceGroup',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='tradingPartner',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='unitOfMeasure',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='valuationGroup',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
