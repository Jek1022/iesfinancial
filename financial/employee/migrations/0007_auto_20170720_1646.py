# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-20 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20170719_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 16, 46, 53, 623000)),
        ),
    ]
