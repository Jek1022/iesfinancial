# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-16 14:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0009_auto_20170504_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 16, 14, 10, 20, 633000)),
        ),
    ]
