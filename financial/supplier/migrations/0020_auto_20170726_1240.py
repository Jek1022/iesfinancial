# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-26 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0019_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 12, 39, 52, 917000)),
        ),
    ]
