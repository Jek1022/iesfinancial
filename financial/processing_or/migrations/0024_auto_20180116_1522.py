# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-16 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_or', '0023_auto_20180115_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs_ormain',
            name='paytype',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='temp_ormain',
            name='paytype',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
