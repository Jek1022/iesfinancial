# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-12 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0027_auto_20171010_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='productgroup',
        ),
        migrations.AlterField(
            model_name='department',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 16, 51, 35, 663000)),
        ),
    ]
