# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-26 03:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountspayable', '0017_auto_20170925_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='apmain',
            name='print_ctr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 973000)),
        ),
        migrations.AlterField(
            model_name='apdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 973000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 977000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 977000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 983000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 983000)),
        ),
        migrations.AlterField(
            model_name='apdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 981000)),
        ),
        migrations.AlterField(
            model_name='apdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 981000)),
        ),
        migrations.AlterField(
            model_name='apmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 26, 11, 20, 32, 964000)),
        ),
    ]
