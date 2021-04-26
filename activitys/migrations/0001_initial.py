# Generated by Django 3.2 on 2021-04-25 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('AC', 'Accounting'), ('PM', 'Project Management'), ('HR', 'Human Resources')], default='', max_length=155)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='Activity Description', max_length=155)),
                ('details', models.CharField(default='Activity Details', max_length=300)),
                ('activity_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activitys', to='activitys.activitycategory')),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
