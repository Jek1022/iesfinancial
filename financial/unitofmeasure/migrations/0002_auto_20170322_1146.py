# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-22 11:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitofmeasure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitofmeasure',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 11, 46, 23, 776453)),
        ),
    ]
