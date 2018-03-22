# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-21 08:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productgroupcategory', '0005_auto_20180110_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroupcategory',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 27, 41, 66000)),
        ),
        migrations.AlterUniqueTogether(
            name='productgroupcategory',
            unique_together=set([('productgroup', 'category')]),
        ),
    ]
