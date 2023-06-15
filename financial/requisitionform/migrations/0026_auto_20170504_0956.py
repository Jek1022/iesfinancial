# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-04 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitionform', '0025_auto_20170426_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfmain',
            name='print_ctr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 9, 56, 40, 13000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 9, 56, 40, 13000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 9, 56, 40, 14000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 9, 56, 40, 14000)),
        ),
        migrations.AlterField(
            model_name='rfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 9, 56, 40, 10000)),
        ),
    ]
