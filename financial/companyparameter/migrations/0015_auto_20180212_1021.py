# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-12 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyparameter', '0014_auto_20180212_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyparameter',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
