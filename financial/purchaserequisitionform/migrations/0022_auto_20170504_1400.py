# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-04 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaserequisitionform', '0021_auto_20170504_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rfprftransaction',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 14, 0, 49, 588000)),
        ),
        migrations.AlterField(
            model_name='prfdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 4, 14, 0, 49, 588000), null=True),
        ),
        migrations.AlterField(
            model_name='prfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 14, 0, 49, 588000)),
        ),
        migrations.AlterField(
            model_name='prfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 14, 0, 49, 588000)),
        ),
        migrations.AlterModelTable(
            name='rfprftransaction',
            table='rfprftransaction',
        ),
    ]
