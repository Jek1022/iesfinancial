# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-05 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0012_auto_20170504_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='fxrate',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 10, 3, 55, 195000)),
        ),
    ]
