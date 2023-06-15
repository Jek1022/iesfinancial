# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-05 10:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0029_auto_20170905_1850'),
        ('operationalfund', '0047_auto_20170905_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofitem',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofitem_supplier_id', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='ofitem',
            name='supplier_code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='ofitem',
            name='supplier_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='ofitemtemp',
            name='supplier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ofitemtemp',
            name='supplier_code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='ofitemtemp',
            name='supplier_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 596000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 600000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 608000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 606000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 593000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 603000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 18, 50, 46, 589000)),
        ),
    ]
