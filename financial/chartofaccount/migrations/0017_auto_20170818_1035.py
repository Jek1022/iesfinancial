# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-18 02:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0016_auto_20170817_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 10, 35, 32, 110000)),
        ),
    ]
