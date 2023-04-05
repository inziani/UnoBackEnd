# Generated by Django 4.0.3 on 2023-04-04 09:01

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0008_remove_taxcode_companycode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralLedgerAccountGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountGroup', models.CharField(max_length=4, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateChanged', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('accountGroup',),
            },
        ),
        migrations.CreateModel(
            name='TaxCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxCode', models.CharField(max_length=2, unique=True)),
                ('taxCodeDescription', models.CharField(max_length=50)),
                ('taxCodePercentage', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5, unique=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateChanged', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('taxCode',),
            },
        ),
    ]
