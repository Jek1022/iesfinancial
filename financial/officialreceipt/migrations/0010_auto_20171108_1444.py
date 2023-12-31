# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-08 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adtype', '0004_auto_20171108_1444'),
        ('officialreceipt', '0009_auto_20171108_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='ormain',
            name='adtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ormain_adtype_id', to='adtype.Adtype'),
        ),
        migrations.AlterField(
            model_name='ordetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 44, 36, 991000)),
        ),
        migrations.AlterField(
            model_name='ordetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 44, 36, 995000)),
        ),
        migrations.AlterField(
            model_name='ordetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 44, 37, 3000)),
        ),
        migrations.AlterField(
            model_name='ordetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 44, 36, 999000)),
        ),
        migrations.AlterField(
            model_name='ormain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 44, 36, 985000)),
        ),
    ]
