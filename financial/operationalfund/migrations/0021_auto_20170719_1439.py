# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-19 14:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0020_auto_20170719_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofmain',
            name='employee_code',
            field=models.CharField(default='011161100', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 19, 14, 39, 5, 784000)),
        ),
    ]
