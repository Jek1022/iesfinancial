# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-06 06:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0021_auto_20171106_1436'),
        ('artype', '0002_auto_20170807_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='artype',
            name='creditchartofaccount',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='artype_creditchartofaccount', to='chartofaccount.Chartofaccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 14, 35, 52, 45000)),
        ),
    ]
