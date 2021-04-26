# Generated by Django 3.2 on 2021-04-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitycategory',
            options={'ordering': ('description',)},
        ),
        migrations.RemoveField(
            model_name='activitycategory',
            name='name',
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='category',
            field=models.CharField(choices=[('PS', 'Personal'), ('OF', 'Official')], default='', max_length=155),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='description',
            field=models.CharField(default='', max_length=155),
            preserve_default=False,
        ),
    ]
