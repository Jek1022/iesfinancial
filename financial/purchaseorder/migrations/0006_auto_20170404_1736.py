# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-04 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0005_auto_20170404_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 17, 36, 51, 439000)),
        ),
        migrations.AlterField(
            model_name='podetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 17, 36, 51, 439000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 17, 36, 51, 442000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 17, 36, 51, 442000)),
        ),
        migrations.AlterField(
            model_name='pomain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 17, 36, 51, 437000)),
        ),
    ]
