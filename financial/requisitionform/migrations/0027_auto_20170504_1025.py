# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-04 10:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitionform', '0026_auto_20170504_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfdetail',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 10, 25, 43, 678000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 10, 25, 43, 678000)),
        ),
        migrations.AlterField(
            model_name='rfdetail',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='enterdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 10, 25, 43, 682000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 10, 25, 43, 683000)),
        ),
        migrations.AlterField(
            model_name='rfdetailtemp',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rfmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 10, 25, 43, 676000)),
        ),
    ]
