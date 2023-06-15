# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-24 07:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0019_auto_20170824_1509'),
        ('ofsubtype', '0007_auto_20170824_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofsubtype',
            name='chartexpcostofsale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofsubtype_chartexpcostofsale', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AddField(
            model_name='ofsubtype',
            name='chartexpgenandadmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofsubtype_chartexpgenandadmin', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AddField(
            model_name='ofsubtype',
            name='chartexpsellexp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofsubtype_chartexpsellexp', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AlterField(
            model_name='ofsubtype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 15, 9, 1, 977000)),
        ),
    ]
