# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-21 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acknowledgementreceipt', '0008_auto_20180321_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='ardetail',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ardetail_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ardetail',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ardetailbreakdown',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ardetailbreakdown_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ardetailbreakdown',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ardetailbreakdowntemp',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ardetailbreakdowntemp_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ardetailbreakdowntemp',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ardetailtemp',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ardetailtemp_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ardetailtemp',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aritem',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aritem_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aritem',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aritemtemp',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aritemtemp_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aritemtemp',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='armain',
            name='closeby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='armain_close', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='armain',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ardetail',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ardetailbreakdown',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ardetailbreakdowntemp',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ardetailtemp',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aritem',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aritemtemp',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='armain',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
