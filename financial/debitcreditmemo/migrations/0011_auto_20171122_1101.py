# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-22 03:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debitcreditmemo', '0010_auto_20171120_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcmain',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='dcdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 757000)),
        ),
        migrations.AlterField(
            model_name='dcdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 757000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 761000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 761000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 767000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 768000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 764000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 764000)),
        ),
        migrations.AlterField(
            model_name='dcmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 1, 42, 753000)),
        ),
    ]
