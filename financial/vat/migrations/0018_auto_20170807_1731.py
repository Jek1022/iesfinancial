# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-07 17:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0017_auto_20170728_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 164000)),
        ),
    ]
