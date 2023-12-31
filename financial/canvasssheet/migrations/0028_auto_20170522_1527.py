# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-22 07:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0012_auto_20170522_1527'),
        ('canvasssheet', '0027_auto_20170522_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='csdetail',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='csdetail_branch_id', to='branch.Branch'),
        ),
        migrations.AddField(
            model_name='csdetailtemp',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='csdetailtemp_branch_id', to='branch.Branch'),
        ),
        migrations.AlterField(
            model_name='csdata',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 15, 26, 56, 444000)),
        ),
        migrations.AlterField(
            model_name='csdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 15, 26, 56, 445000)),
        ),
        migrations.AlterField(
            model_name='csdetail',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 22, 15, 26, 56, 446000), null=True),
        ),
        migrations.AlterField(
            model_name='csdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 15, 26, 56, 449000)),
        ),
        migrations.AlterField(
            model_name='csdetailtemp',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 22, 15, 26, 56, 449000), null=True),
        ),
        migrations.AlterField(
            model_name='csmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 15, 26, 56, 440000)),
        ),
    ]
