# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-07 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsubtype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arsubtype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 22, 50, 59, 803000)),
        ),
    ]
