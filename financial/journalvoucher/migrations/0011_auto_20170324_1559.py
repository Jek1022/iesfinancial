# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-24 15:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalvoucher', '0010_auto_20170228_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 36708)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 36796)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='bankaccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount_jvdetailtemp_id', to='bankaccount.Bankaccount'),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 39751)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 39835)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 33813)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 15, 59, 43, 33902)),
        ),
    ]
