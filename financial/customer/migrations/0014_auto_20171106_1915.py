# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-06 11:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20171011_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 19, 14, 57, 453000)),
        ),
    ]
