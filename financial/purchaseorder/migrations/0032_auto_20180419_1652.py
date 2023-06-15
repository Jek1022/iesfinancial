# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-04-19 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0031_auto_20180419_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podetail',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='podetail_branch_id', to='branch.Branch'),
        ),
        migrations.AlterField(
            model_name='podetailtemp',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='podetailtemp_branch_id', to='branch.Branch'),
        ),
    ]
