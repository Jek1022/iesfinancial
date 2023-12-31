# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-10-19 03:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20171019_1134'),
        ('operationalfund', '0056_auto_20171019_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofmain',
            name='actualapprover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofmain_actual_approver', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='ofmain',
            name='designatedapprover',
            field=models.ForeignKey(default=493, on_delete=django.db.models.deletion.CASCADE, related_name='ofmain_designated_approver', to='employee.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ofmain',
            name='requestor',
            field=models.ForeignKey(default=717, on_delete=django.db.models.deletion.CASCADE, related_name='ofmain_requestor_id', to='employee.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ofmain',
            name='requestor_code',
            field=models.CharField(default='011161100', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ofmain',
            name='requestor_name',
            field=models.CharField(default='REY KENNETH MOLINA', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ofdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 138000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 142000)),
        ),
        migrations.AlterField(
            model_name='ofdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 152000)),
        ),
        migrations.AlterField(
            model_name='ofdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 149000)),
        ),
        migrations.AlterField(
            model_name='ofitem',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 135000)),
        ),
        migrations.AlterField(
            model_name='ofitemtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 146000)),
        ),
        migrations.AlterField(
            model_name='ofmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 11, 33, 46, 129000)),
        ),
    ]
