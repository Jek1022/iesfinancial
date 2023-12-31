# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-24 06:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaserequisitionform', '0038_auto_20170524_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='prfdetailtemp',
            name='estimateddateofdelivery',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 21, 48, 362000)),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 24, 14, 21, 48, 363000), null=True),
        ),
        migrations.AlterField(
            model_name='prfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 21, 48, 368000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 21, 48, 352000)),
        ),
    ]
