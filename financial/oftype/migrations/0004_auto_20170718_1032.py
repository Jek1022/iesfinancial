# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-18 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oftype', '0003_auto_20170718_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oftype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 10, 32, 26, 573000)),
        ),
    ]
