# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-08 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0025_auto_20180208_1623'),
        ('processing_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poapvtransaction',
            name='podetail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='podetail_poapvtransaction', to='purchaseorder.Podetail'),
            preserve_default=False,
        ),
    ]
