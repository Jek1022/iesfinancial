# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-15 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccountmaingroup', '0005_chartofaccountmaingroup_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartofaccountmaingroup',
            name='title',
        ),
    ]
