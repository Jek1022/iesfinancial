# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-19 06:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankbranchdisburse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankbranchdisburse',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='bankbranchdisburse',
            name='address2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bankbranchdisburse',
            name='address3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bankbranchdisburse',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 14, 1, 55, 212000)),
        ),
    ]
