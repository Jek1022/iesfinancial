# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-18 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountexpensebalance', '0002_auto_20180518_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountexpensebalance',
            name='transactionnum',
            field=models.CharField(default='jv', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountexpensebalance',
            name='transactiontype',
            field=models.CharField(default='jv', max_length=2),
            preserve_default=False,
        ),
    ]
