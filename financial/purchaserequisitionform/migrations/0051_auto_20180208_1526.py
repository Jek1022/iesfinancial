# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-08 07:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaserequisitionform', '0050_auto_20180131_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 26, 20, 39000)),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 8, 15, 26, 20, 39000), null=True),
        ),
        migrations.AlterField(
            model_name='prfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 26, 20, 43000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 26, 20, 34000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
