# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-10 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputvattype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outputvattype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 19, 50, 54, 945000)),
        ),
    ]
