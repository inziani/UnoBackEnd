# Generated by Django 3.2.6 on 2021-11-23 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitys', '0003_auto_20210804_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='slug',
        ),
    ]