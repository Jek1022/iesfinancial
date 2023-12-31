# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-18 01:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsadjustment', '0003_auto_20171122_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmitem',
            name='amount',
        ),
        migrations.AddField(
            model_name='cmitem',
            name='creditamount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AddField(
            model_name='cmitem',
            name='debitamount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='cmitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 9, 26, 41, 173000)),
        ),
        migrations.AlterField(
            model_name='cmmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 9, 26, 41, 169000)),
        ),
    ]
