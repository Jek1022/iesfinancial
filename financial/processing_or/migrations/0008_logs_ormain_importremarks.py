# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-13 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_or', '0007_logs_ormain_importstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs_ormain',
            name='importremarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
