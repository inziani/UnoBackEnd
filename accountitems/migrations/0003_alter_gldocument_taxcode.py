# Generated by Django 4.0.3 on 2023-03-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountitems', '0002_alter_glaccountlineitems_accountnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gldocument',
            name='taxCode',
            field=models.CharField(max_length=2),
        ),
    ]