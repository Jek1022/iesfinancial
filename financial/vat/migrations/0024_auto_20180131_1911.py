# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-31 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0023_auto_20180131_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 31, 19, 11, 15, 128000)),
        ),
    ]
