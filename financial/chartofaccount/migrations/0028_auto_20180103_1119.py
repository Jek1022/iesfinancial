# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-03 03:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0027_auto_20171219_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 3, 11, 18, 46, 202000)),
        ),
    ]
