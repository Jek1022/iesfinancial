# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-23 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_auto_20170320_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 10, 33, 16, 443000)),
        ),
    ]
