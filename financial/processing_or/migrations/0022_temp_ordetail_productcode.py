# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-10 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_or', '0021_temp_ormain_accounttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_ordetail',
            name='productcode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
