# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-17 09:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0015_auto_20170817_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 17, 39, 48, 141000)),
        ),
    ]
