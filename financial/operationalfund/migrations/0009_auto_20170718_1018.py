# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-18 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0008_auto_20170718_1018'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='ofmain',
        #     name='oftype',
        # ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 10, 18, 49, 778000)),
        ),
    ]
