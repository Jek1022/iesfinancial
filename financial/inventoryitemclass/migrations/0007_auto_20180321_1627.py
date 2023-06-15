# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-21 08:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryitemclass', '0006_auto_20171109_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitemclass',
            name='chartofaccountinventory',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='invclass_chartofaccountinv_id', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AlterField(
            model_name='inventoryitemclass',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 40, 914000)),
        ),
    ]
