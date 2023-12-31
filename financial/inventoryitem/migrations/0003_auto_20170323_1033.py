# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-23 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryitem', '0002_auto_20170322_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='expensestatus',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='specialstatus',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='stocklevel',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='code',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 10, 33, 16, 564000)),
        ),
    ]
