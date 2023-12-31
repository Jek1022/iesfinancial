# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-21 08:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkvoucher', '0023_auto_20180307_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 3000)),
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 4000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 6000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 6000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 11000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 11000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 9000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 9000)),
        ),
        migrations.AlterField(
            model_name='cvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 1000)),
        ),
    ]
