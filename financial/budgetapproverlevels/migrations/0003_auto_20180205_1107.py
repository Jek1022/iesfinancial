# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-05 03:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetapproverlevels', '0002_auto_20180205_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetapproverlevels',
            name='expwithinbudget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='budgetapproverlevels',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 5, 11, 7, 22, 212000)),
        ),
    ]
