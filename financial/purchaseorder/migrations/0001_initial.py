# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-03 15:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creditterm', '0002_auto_20170403_1552'),
        ('vat', '0003_auto_20170403_1552'),
        ('inputvat', '0003_auto_20170403_1552'),
        ('ataxcode', '0003_auto_20170403_1552'),
        ('supplier', '0004_auto_20170403_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponum', models.CharField(max_length=10, unique=True)),
                ('podate', models.DateField()),
                ('refnum', models.CharField(blank=True, max_length=150, null=True)),
                ('potype', models.CharField(default='REGULAR', max_length=150)),
                ('urgencytype', models.CharField(choices=[('N', 'Normal'), ('R', 'Rush')], default='N', max_length=1)),
                ('dateneeded', models.DateField()),
                ('particulars', models.TextField()),
                ('postatus', models.CharField(choices=[('F', 'For Approval'), ('A', 'Approved'), ('D', 'Disapproved')], default='F', max_length=1)),
                ('approverresponse', models.CharField(blank=True, choices=[('A', 'Approved'), ('D', 'Disapproved')], max_length=1, null=True)),
                ('responsedate', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('supplier_code', models.CharField(max_length=25)),
                ('supplier_name', models.CharField(max_length=250)),
                ('apnum', models.CharField(blank=True, max_length=150, null=True)),
                ('apdate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 4, 3, 15, 52, 57, 937000))),
                ('postdate', models.DateTimeField(blank=True, null=True)),
                ('isdeleted', models.IntegerField(default=0)),
                ('actualapprover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_actual_approver', to=settings.AUTH_USER_MODEL)),
                ('ataxcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_ataxcode_id', to='ataxcode.Ataxcode')),
                ('creditterm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_creditterm_id', to='creditterm.Creditterm')),
                ('designatedapprover', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_designated_approver', to=settings.AUTH_USER_MODEL)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_enter', to=settings.AUTH_USER_MODEL)),
                ('inputvat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_inputvat_id', to='inputvat.Inputvat')),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_modify', to=settings.AUTH_USER_MODEL)),
                ('postby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomain_post', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pomain_supplier_id', to='supplier.Supplier')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pomain_vat_id', to='vat.Vat')),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'pomain',
            },
        ),
    ]
