# Generated by Django 4.0.3 on 2024-05-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0022_alter_generalledgeraccountmaster_reconciliationaccounttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalledgeraccountmaster',
            name='alternativeGLAccount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]