# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-03 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 3, 16, 40, 19, 393000)),
        ),
    ]
