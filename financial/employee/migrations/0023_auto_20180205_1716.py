# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-05 09:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetapproverlevels', '0010_auto_20180205_1716'),
        ('employee', '0022_auto_20180123_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='managementlevel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budgetapproverlevels_id', to='budgetapproverlevels.Budgetapproverlevels'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 5, 17, 16, 21, 452000)),
        ),
    ]
