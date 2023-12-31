# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-19 02:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountspayable', '0008_auto_20170919_1040'),
        ('operationalfund', '0053_auto_20170919_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reprfvdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 9, 19, 10, 40, 43, 562000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('print_ctr', models.IntegerField(default=0)),
                ('apmain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvdetail_apmain_id', to='accountspayable.Apmain')),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvdetail_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvdetail_modify', to=settings.AUTH_USER_MODEL)),
                ('ofmain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reprfvdetail_ofmain_id', to='operationalfund.Ofmain')),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'reprfvdetail',
            },
        ),
        migrations.CreateModel(
            name='Reprfvmain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reprfvnum', models.CharField(max_length=10, unique=True)),
                ('reprfvdate', models.DateField()),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 9, 19, 10, 40, 43, 561000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('print_ctr', models.IntegerField(default=0)),
                ('apmain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvmain_apmain_id', to='accountspayable.Apmain')),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvmain_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reprfvmain_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'reprfvmain',
                'permissions': (('view_replenish_rfv', 'Can view replenishment of RFV'),),
            },
        ),
        migrations.AddField(
            model_name='reprfvdetail',
            name='reprfvmain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reprfvdetail_reprfvmain_id', to='replenish_rfv.Reprfvmain'),
        ),
    ]
