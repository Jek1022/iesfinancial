# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-24 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0015_auto_20170324_1625'),
        ('journalvoucher', '0021_auto_20170324_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jvdetailtemp',
            name='departmentxxxx',
        ),
        migrations.AddField(
            model_name='jvdetailtemp',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_jvdetailtemp_id', to='department.Department'),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 616620)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 616705)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 620258)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 620343)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 613737)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 25, 23, 613825)),
        ),
    ]
