# Generated by Django 4.0.3 on 2023-03-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0005_alter_generalledgeraccountmaster_businessarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='accountType',
            field=models.CharField(choices=[('Assets', 'Assets'), ('Accounts Payables', 'Accounts Payable'), ('Accounts Receivables', 'Accounts Receivable'), ('Materials', 'Materials'), ('General Ledger', 'General Ledger')], max_length=30),
        ),
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='reconciliationAccountType',
            field=models.CharField(choices=[('Assets', 'Assets'), ('Accounts Payables', 'Accounts Payable'), ('Accounts Receivables', 'Accounts Receivable'), ('Materials', 'Materials'), ('Not Required', 'Not Required')], max_length=30),
        ),
    ]