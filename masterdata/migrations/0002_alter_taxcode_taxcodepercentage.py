# Generated by Django 4.0.1 on 2022-01-26 06:41

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxcode',
            name='taxCodePercentage',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5, unique=True),
        ),
    ]
