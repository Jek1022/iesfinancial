# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-23 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0037_auto_20180321_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartofaccount',
            name='beginning_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='beginning_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='beginning_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='end_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='end_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='year_to_date_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='year_to_date_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='year_to_date_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
