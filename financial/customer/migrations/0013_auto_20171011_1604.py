# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-11 08:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20171010_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 11, 16, 2, 15, 631000)),
        ),
    ]
