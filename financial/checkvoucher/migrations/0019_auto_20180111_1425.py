# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-11 06:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkvoucher', '0018_auto_20180103_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvmain',
            name='releaseto',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 683000)),
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 683000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 687000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 687000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 696000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 696000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 691000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 691000)),
        ),
        migrations.AlterField(
            model_name='cvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 14, 25, 39, 678000)),
        ),
    ]
