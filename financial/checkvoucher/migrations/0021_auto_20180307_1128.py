# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-07 03:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkvoucher', '0020_auto_20180112_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 196000)),
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 196000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 199000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 199000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 202000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 202000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 201000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 201000)),
        ),
        migrations.AlterField(
            model_name='cvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 11, 28, 31, 193000)),
        ),
    ]
