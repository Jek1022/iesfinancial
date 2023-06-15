# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-21 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountexpensebalance', '0003_auto_20180518_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountexpensebalance',
            name='transactionnum',
        ),
        migrations.RemoveField(
            model_name='accountexpensebalance',
            name='transactiontype',
        ),
        migrations.AddField(
            model_name='accountexpensebalance',
            name='unit',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
