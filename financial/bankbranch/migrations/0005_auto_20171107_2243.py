# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-07 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankbranch', '0004_auto_20171107_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankbranch',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 22, 43, 20, 682000)),
        ),
    ]
