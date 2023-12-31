# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-15 13:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debitcreditmemo', '0003_auto_20170815_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 152000)),
        ),
        migrations.AlterField(
            model_name='dcdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 153000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 157000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 157000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 162000)),
        ),
        migrations.AlterField(
            model_name='dcdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 162000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 160000)),
        ),
        migrations.AlterField(
            model_name='dcdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 160000)),
        ),
        migrations.AlterField(
            model_name='dcmain',
            name='dctype',
            field=models.CharField(choices=[('D', 'Debit Memo'), ('C', 'Credit Memo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='dcmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 33, 22, 149000)),
        ),
    ]
