# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-15 13:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debitcreditmemo', '0002_auto_20170811_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcmain',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='dcmain',
            name='employee_code',
        ),
        migrations.RemoveField(
            model_name='dcmain',
            name='employee_name',
        ),
        migrations.AlterField(
            model_name='dcdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 384000)),
        ),
        migrations.AlterField(
            model_name='dcdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 384000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 388000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 388000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 394000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 394000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 391000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 391000)),
        ),
        migrations.AlterField(
            model_name='dcmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 24, 59, 381000)),
        ),
    ]
