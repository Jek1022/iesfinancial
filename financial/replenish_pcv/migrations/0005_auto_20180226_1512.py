# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-26 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replenish_pcv', '0004_auto_20180223_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reppcvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 26, 15, 12, 13, 563000)),
        ),
        migrations.AlterField(
            model_name='reppcvmain',
            name='finalapproverremarks',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='reppcvmain',
            name='initialapproverremarks',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='reppcvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 26, 15, 12, 13, 561000)),
        ),
    ]
