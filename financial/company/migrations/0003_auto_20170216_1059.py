# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-16 10:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170216_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 59, 4, 995000)),
        ),
    ]
