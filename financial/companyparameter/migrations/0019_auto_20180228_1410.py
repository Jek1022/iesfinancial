# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofsubtype', '0009_auto_20180228_1410'),
        ('companyparameter', '0018_auto_20180223_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyparameter',
            name='pcv_meal_budget_limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.AddField(
            model_name='companyparameter',
            name='pcv_meal_expenses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companyparameter_pcv_meal_expenses', to='ofsubtype.Ofsubtype'),
        ),
    ]
