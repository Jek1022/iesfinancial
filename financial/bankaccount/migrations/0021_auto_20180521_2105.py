# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-21 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0020_auto_20180322_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='year_to_date_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='year_to_date_code',
            field=models.CharField(blank=True, choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='year_to_date_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
