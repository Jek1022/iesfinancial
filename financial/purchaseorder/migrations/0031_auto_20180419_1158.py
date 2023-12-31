# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-04-19 03:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0030_auto_20180321_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomain',
            name='dateneeded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pomain',
            name='wtax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_wtax_id', to='wtax.Wtax', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
