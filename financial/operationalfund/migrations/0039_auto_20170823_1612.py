# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-23 08:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofsubtype', '0006_auto_20170823_1612'),
        ('operationalfund', '0038_auto_20170823_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofitemtemp',
            name='ofsubtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofitemtemp_ofsubtype_id', to='ofsubtype.Ofsubtype'),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 394000)),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 394000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 399000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 399000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 408000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 408000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 405000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 405000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 389000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 389000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 403000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 403000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 12, 50, 384000)),
        ),
    ]
