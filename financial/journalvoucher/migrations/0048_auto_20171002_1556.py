# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-02 07:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalvoucher', '0047_auto_20171002_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='jvmain',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 719000)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 720000)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 723000)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 724000)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 732000)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 732000)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 727000)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 727000)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 715000)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 15, 56, 49, 715000)),
        ),
    ]
