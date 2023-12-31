# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-05 08:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaserequisitionform', '0047_auto_20170605_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='prfdetail',
            name='csdetail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prfdetailtemp',
            name='csdetail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 16, 3, 45, 489000)),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 5, 16, 3, 45, 489000), null=True),
        ),
        migrations.AlterField(
            model_name='prfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 16, 3, 45, 497000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 16, 3, 45, 476000)),
        ),
    ]
