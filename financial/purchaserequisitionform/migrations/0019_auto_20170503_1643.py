# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-03 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaserequisitionform', '0018_auto_20170503_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='prfdetail',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='prfdetailtemp',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 43, 7, 743000)),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 3, 16, 43, 7, 744000), null=True),
        ),
        migrations.AlterField(
            model_name='prfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 43, 7, 747000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 43, 7, 737000)),
        ),
    ]
