# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-24 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalvoucher', '0018_auto_20170324_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jvdetailtemp',
            name='department_id',
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 527277)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 527394)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 531355)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 531446)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 523675)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 16, 21, 31, 523786)),
        ),
    ]
