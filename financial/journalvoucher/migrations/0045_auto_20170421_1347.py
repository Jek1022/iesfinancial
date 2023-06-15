# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-21 13:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalvoucher', '0044_auto_20170421_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jvdetail',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 682915)),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jvdetail_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jvdetail',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 683026)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 688150)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jvdetailbreakdown_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdown',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 688264)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 695483)),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jvdetailbreakdowntemp_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jvdetailbreakdowntemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 695580)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 692190)),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jvdetailtemp_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jvdetailtemp',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 692296)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 678782)),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jvmain_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jvmain',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 13, 47, 0, 678919)),
        ),
    ]
