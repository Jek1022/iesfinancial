# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-03 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountspayable', '0031_auto_20180321_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apmain',
            name='creditterm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ap_creditterm_id', to='creditterm.Creditterm'),
        ),
    ]
