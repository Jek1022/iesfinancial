# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-26 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0032_auto_20180222_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartofaccount',
            name='refdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='refnum',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='reftype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
