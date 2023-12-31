# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-04 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitionform', '0028_auto_20170504_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfdetail',
            name='isfullyprf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rfdetail',
            name='prfremainingquantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rfdetail',
            name='prftotalquantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rfmain',
            name='totalremainingquantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 6, 425000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 6, 425000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 6, 427000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 6, 429000)),
        ),
        migrations.AlterField(
            model_name='rfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 6, 422000)),
        ),
    ]
