# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-20 14:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalvoucher', '0040_auto_20170420_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jvdetailtemp',
            name='particular',
        ),
        migrations.AddField(
            model_name='jvdetailbreakdown',
            name='particular',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 445116)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 445210)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 449356)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 449447)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 456047)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 456135)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 453312)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 453403)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 441520)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 29, 58, 441630)),
        ),
    ]
