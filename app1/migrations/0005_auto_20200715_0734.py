# Generated by Django 3.0.3 on 2020-07-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_enrollsubjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollsubjects',
            name='no',
        ),
        migrations.AddField(
            model_name='enrollsubjects',
            name='c_name',
            field=models.CharField(default=None, max_length=40, unique=True),
        ),
    ]
