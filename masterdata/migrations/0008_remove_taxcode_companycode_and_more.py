# Generated by Django 4.0.3 on 2023-03-27 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountitems', '0003_alter_gldocument_taxcode'),
        ('masterdata', '0007_alter_generalledgeraccountmaster_accountgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxcode',
            name='companyCode',
        ),
        migrations.DeleteModel(
            name='GeneralLedgerAccountGroup',
        ),
        migrations.DeleteModel(
            name='TaxCode',
        ),
    ]