# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-25 07:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountspayable', '0012_auto_20170925_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 299000)),
        ),
        migrations.AlterField(
            model_name='apdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 299000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 303000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 303000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 310000)),
        ),
        migrations.AlterField(
            model_name='apdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 310000)),
        ),
        migrations.AlterField(
            model_name='apdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 306000)),
        ),
        migrations.AlterField(
            model_name='apdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 307000)),
        ),
        migrations.AlterField(
            model_name='apmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 25, 15, 13, 46, 292000)),
        ),
        migrations.AlterField(
            model_name='apmain',
            name='refno',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
