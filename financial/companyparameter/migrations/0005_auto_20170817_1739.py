# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-17 09:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyparameter', '0004_auto_20170817_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyparameter',
            name='coa_inputtax',
        ),
        migrations.AlterField(
            model_name='companyparameter',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 17, 39, 6, 921000)),
        ),
    ]
