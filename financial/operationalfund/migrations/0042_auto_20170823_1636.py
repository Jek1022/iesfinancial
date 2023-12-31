# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-23 08:36
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ataxcode', '0016_auto_20170823_1636'),
        ('operationalfund', '0041_auto_20170823_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofitem',
            name='atc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofitem_atc_id', to='ataxcode.Ataxcode', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='ofitem',
            name='atcrate',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='ofitemtemp',
            name='atc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ofitemtemp',
            name='atcrate',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 826000)),
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 826000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 830000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 831000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 839000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 839000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 836000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 836000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 823000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 823000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 834000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 834000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 36, 31, 819000)),
        ),
    ]
