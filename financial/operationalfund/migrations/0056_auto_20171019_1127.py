# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-19 03:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0055_auto_20171002_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofmain',
            name='actualapprover',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='designatedapprover',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='requestor',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='requestor_name',
        ),
        migrations.RemoveField(
            model_name='ofmain',
            name='requestor_username',
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 922000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 926000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 935000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 933000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 918000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 930000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 27, 49, 914000)),
        ),
    ]
