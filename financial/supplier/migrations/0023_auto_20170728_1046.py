# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-28 10:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0022_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='bankaccountname',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='bankaccountnumber',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='bankaccounttype',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 10, 46, 3, 597000)),
        ),
    ]
