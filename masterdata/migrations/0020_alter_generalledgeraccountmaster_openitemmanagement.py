# Generated by Django 4.0.3 on 2024-03-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0019_alter_generalledgeraccountmaster_tradingpartner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='openItemManagement',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
