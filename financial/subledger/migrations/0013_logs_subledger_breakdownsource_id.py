# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-04 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subledger', '0012_subledger_breakdownsource_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs_subledger',
            name='breakdownsource_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
