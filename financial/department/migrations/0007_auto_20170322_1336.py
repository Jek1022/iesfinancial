# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-22 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_auto_20170320_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='expchartofaccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount_department', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AlterField(
            model_name='department',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 13, 36, 37, 69000)),
        ),
    ]
