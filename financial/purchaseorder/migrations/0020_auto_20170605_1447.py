# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-05 14:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0019_auto_20170526_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podata',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 608000)),
        ),
        migrations.AlterField(
            model_name='podetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 601000)),
        ),
        migrations.AlterField(
            model_name='podetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 602000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 605000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 605000)),
        ),
        migrations.AlterField(
            model_name='pomain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 14, 47, 28, 596000)),
        ),
    ]
