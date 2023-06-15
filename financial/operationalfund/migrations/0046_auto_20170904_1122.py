# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-04 03:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalfund', '0045_auto_20170829_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ofmain',
            old_name='print_ctr',
            new_name='print_ctr1',
        ),
        migrations.AddField(
            model_name='ofmain',
            name='print_ctr2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 259000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 264000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 273000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 270000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 256000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 268000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 11, 22, 7, 252000)),
        ),
    ]
