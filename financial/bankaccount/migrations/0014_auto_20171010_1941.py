# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-10 11:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0013_auto_20170817_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 19, 41, 37, 528000)),
        ),
    ]
