# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-10 12:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requisitionform', '0018_auto_20170410_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfdetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 12, 38, 33, 458000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 12, 38, 33, 458000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 12, 38, 33, 459000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 12, 38, 33, 459000)),
        ),
        migrations.AlterField(
            model_name='rfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 12, 38, 33, 455000)),
        ),
    ]
