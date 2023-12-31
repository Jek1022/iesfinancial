# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-31 09:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chartofaccount', '0001_initial'),
        ('currency', '0001_initial'),
        ('bankaccounttype', '0001_initial'),
        ('bank', '0001_initial'),
        ('bankbranch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('accountnumber', models.CharField(max_length=30)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('beg_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('beg_code', models.CharField(blank=True, choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1, null=True)),
                ('beg_date', models.DateField(blank=True, null=True)),
                ('run_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('run_code', models.CharField(blank=True, choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1, null=True)),
                ('run_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 31, 17, 15, 47, 541435))),
                ('isdeleted', models.IntegerField(default=0)),
                ('bank', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bank_id', to='bank.Bank', validators=[django.core.validators.MinValueValidator(1)])),
                ('bankaccounttype', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccounttype_id', to='bankaccounttype.Bankaccounttype', validators=[django.core.validators.MinValueValidator(1)])),
                ('bankbranch', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bankbranch_id', to='bankbranch.Bankbranch', validators=[django.core.validators.MinValueValidator(1)])),
                ('chartofaccount', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount_id', to='chartofaccount.Chartofaccount', validators=[django.core.validators.MinValueValidator(1)])),
                ('currency', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_id', to='currency.Currency', validators=[django.core.validators.MinValueValidator(1)])),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'bankaccount',
                'permissions': (('view_bankaccount', 'Can view bankaccount'),),
            },
        ),
    ]
