# Generated by Django 4.0.3 on 2024-03-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0018_alter_generalledgeraccountmaster_tradingpartner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='tradingPartner',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
