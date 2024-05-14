# Generated by Django 4.0.3 on 2024-05-14 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_landline_alter_company_mobilenumber'),
        ('masterdata', '0024_alter_generalledgeraccountmaster_costelement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='accountGroup',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='authorizationGroup',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='balancesInLocalCurrency',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='blockedForPosting',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='businessArea',
            field=models.ForeignKey(blank=True, max_length=4, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='GeneralLedgerAccountMaster', to='company.businessarea'),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='controllingArea',
            field=models.ForeignKey(blank=True, max_length=4, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='GeneralLedgerAccountMaster', to='company.controllingarea'),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='costElement',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='exchangeRateKey',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='fieldStatusGroup',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='groupAccountNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='houseBank',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='houseBankAccountID',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='inflationKey',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='lineItemManagement',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='markedForDeletion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='planningLevel',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='postAutomaticallyOnly',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='postingWithoutTaxAllowed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='reconciliationAccountInput',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='reconciliationAccountType',
            field=models.CharField(choices=[('Assets', 'Assets'), ('Accounts Payables', 'Accounts Payable'), ('Accounts Receivables', 'Accounts Receivable'), ('Materials', 'Materials'), ('General Ledger', 'General Ledger')], max_length=30),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='relevantToCashFlow',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='sortKey',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='supplementAutomaticPostings',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='taxCategory',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='toleranceGroup',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='tradingPartner',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='unitOfMeasure',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='valuationGroup',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
