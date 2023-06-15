# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-10 12:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officialreceipt', '0003_auto_20171010_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='ormain',
            name='customer_code',
            field=models.CharField(default='TEST', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 77000)),
        ),
        migrations.AlterField(
            model_name='ordetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 81000)),
        ),
        migrations.AlterField(
            model_name='ordetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 90000)),
        ),
        migrations.AlterField(
            model_name='ordetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 87000)),
        ),
        migrations.AlterField(
            model_name='oritem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 74000)),
        ),
        migrations.AlterField(
            model_name='oritemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 85000)),
        ),
        migrations.AlterField(
            model_name='ormain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 20, 58, 7, 70000)),
        ),
    ]
