# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-21 08:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptype', '0003_auto_20180321_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 56, 3, 178000)),
        ),
    ]
