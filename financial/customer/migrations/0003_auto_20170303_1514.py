# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-03 15:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170227_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 3, 15, 14, 26, 865000)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='multiplestatus',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1, null=True),
        ),
    ]
