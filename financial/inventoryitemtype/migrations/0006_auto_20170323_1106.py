# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-23 11:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryitemtype', '0005_auto_20170323_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitemtype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 11, 6, 23, 92000)),
        ),
    ]
