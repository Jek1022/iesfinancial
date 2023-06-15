# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-28 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0010_auto_20170728_1606'),
        ('checkvoucher', '0006_auto_20170728_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvmain',
            name='bankaccountname',
        ),
        migrations.RemoveField(
            model_name='cvmain',
            name='bankaccountnumber',
        ),
        migrations.AddField(
            model_name='cvmain',
            name='bankaccount',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='cvmain_bankaccount_id', to='bankaccount.Bankaccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 547000)),
        ),
        migrations.AlterField(
            model_name='cvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 548000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 552000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 552000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 558000)),
        ),
        migrations.AlterField(
            model_name='cvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 558000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 555000)),
        ),
        migrations.AlterField(
            model_name='cvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 555000)),
        ),
        migrations.AlterField(
            model_name='cvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 16, 5, 53, 543000)),
        ),
    ]
