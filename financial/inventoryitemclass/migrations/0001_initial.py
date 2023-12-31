# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-21 12:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chartofaccount', '0007_auto_20170321_1255'),
        ('inventoryitemtype', '0002_auto_20170321_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventoryitemclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 3, 21, 12, 55, 18, 349941))),
                ('isdeleted', models.IntegerField(default=0)),
                ('chartexpcostofsale', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='chartexpcostofsale_id', to='chartofaccount.Chartofaccount')),
                ('chartexpgenandadmin', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='chartexpgenandadmin_id', to='chartofaccount.Chartofaccount')),
                ('chartexpsellexp', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='chartexpsellexp_id', to='chartofaccount.Chartofaccount')),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inventoryitemclass_enter', to=settings.AUTH_USER_MODEL)),
                ('inventoryitemtype', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='inventoryitemtype_id', to='inventoryitemtype.Inventoryitemtype')),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inventoryitemclass_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'inventoryitemclass',
                'permissions': (('view_inventoryitemclass', 'Can view inventoryitemclass'),),
            },
        ),
    ]
