# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-10 08:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0029_auto_20180110_1649'),
        ('companyparameter', '0011_auto_20180110_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyparameter',
            name='coa_aptrade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_coa_aptrade', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AddField(
            model_name='companyparameter',
            name='coa_ewtax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_coa_ewtax', to='chartofaccount.Chartofaccount'),
        ),
        migrations.AlterField(
            model_name='companyparameter',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 16, 49, 14, 573000)),
        ),
    ]
