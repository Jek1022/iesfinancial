# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-07 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ataxcode', '0003_auto_20170403_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ataxcode',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 7, 17, 32, 40, 403994)),
        ),
    ]
