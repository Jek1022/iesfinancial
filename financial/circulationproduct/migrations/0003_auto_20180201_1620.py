# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-01 08:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulationproduct', '0002_auto_20171107_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circulationproduct',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 16, 20, 50, 588000)),
        ),
    ]
