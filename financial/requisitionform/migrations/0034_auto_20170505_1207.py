# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-05 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitionform', '0033_auto_20170504_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfdetail',
            name='rfprftransaction',
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 12, 7, 6, 297000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 12, 7, 6, 297000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 12, 7, 6, 302000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 12, 7, 6, 302000)),
        ),
        migrations.AlterField(
            model_name='rfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 12, 7, 6, 294000)),
        ),
    ]
