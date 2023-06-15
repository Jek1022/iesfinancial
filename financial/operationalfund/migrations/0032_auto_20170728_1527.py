# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-28 15:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0031_auto_20170728_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 973000)),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 973000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 977000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 977000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 984000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 984000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 981000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 981000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 15, 27, 50, 969000)),
        ),
    ]
