# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-27 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0028_auto_20170720_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofmain',
            name='wtax',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='wtaxamount',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='wtaxrate',
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 27, 15, 36, 27, 219000)),
        ),
    ]
