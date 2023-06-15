# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-31 09:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oftype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 31, 17, 15, 47, 587830))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='oftype_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='oftype_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'oftype',
                'permissions': (('view_oftype', 'Can view oftype'),),
            },
        ),
    ]
