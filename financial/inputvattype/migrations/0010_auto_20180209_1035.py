# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-09 02:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputvattype', '0009_auto_20180209_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputvattype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 10, 35, 25, 884000)),
        ),
    ]
