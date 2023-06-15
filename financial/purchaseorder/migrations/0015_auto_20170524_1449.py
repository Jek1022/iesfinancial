# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-24 14:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0014_auto_20170519_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='podetail',
            name='itemdetailkey',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podetailtemp',
            name='itemdetailkey',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='podata',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 873000)),
        ),
        migrations.AlterField(
            model_name='podetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 865000)),
        ),
        migrations.AlterField(
            model_name='podetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 865000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 869000)),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 869000)),
        ),
        migrations.AlterField(
            model_name='pomain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 14, 48, 59, 859000)),
        ),
    ]
