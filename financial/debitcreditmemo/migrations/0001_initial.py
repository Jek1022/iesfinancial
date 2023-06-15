# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-07 17:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wtax', '0010_auto_20170807_1731'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankaccount', '0011_auto_20170807_1731'),
        ('product', '0008_auto_20170807_1731'),
        ('debitcreditmemosubtype', '0001_initial'),
        ('chartofaccount', '0014_auto_20170807_1731'),
        ('ataxcode', '0015_auto_20170807_1731'),
        ('department', '0026_auto_20170807_1731'),
        ('unit', '0014_auto_20170807_1731'),
        ('employee', '0012_auto_20170807_1731'),
        ('customer', '0011_auto_20170807_1731'),
        ('inputvat', '0009_auto_20170807_1731'),
        ('outputvat', '0008_auto_20170807_1731'),
        ('vat', '0018_auto_20170807_1731'),
        ('branch', '0021_auto_20170807_1731'),
        ('artype', '0002_auto_20170807_1731'),
        ('supplier', '0027_auto_20170807_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dcdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_counter', models.IntegerField()),
                ('dc_num', models.CharField(max_length=10)),
                ('dc_date', models.DateTimeField()),
                ('debitamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('creditamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('balancecode', models.CharField(blank=True, max_length=1, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 449000))),
                ('postdate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 449000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('customerbreakstatus', models.IntegerField(blank=True, null=True)),
                ('supplierbreakstatus', models.IntegerField(blank=True, null=True)),
                ('employeebreakstatus', models.IntegerField(blank=True, null=True)),
                ('ataxcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ataxcode_dcdetail_id', to='ataxcode.Ataxcode')),
                ('bankaccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount_dcdetail_id', to='bankaccount.Bankaccount')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_dcdetail_id', to='branch.Branch')),
                ('chartofaccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount_dcdetail_id', to='chartofaccount.Chartofaccount')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_dcdetail_id', to='customer.Customer')),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'dcdetail',
            },
        ),
        migrations.CreateModel(
            name='Dcdetailbreakdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_counter', models.IntegerField()),
                ('datatype', models.CharField(blank=True, max_length=1, null=True)),
                ('dc_num', models.CharField(max_length=10)),
                ('dc_date', models.DateTimeField()),
                ('particular', models.TextField(blank=True, null=True)),
                ('debitamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('creditamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('balancecode', models.CharField(blank=True, max_length=1, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 452000))),
                ('postdate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 453000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('customerbreakstatus', models.IntegerField(blank=True, null=True)),
                ('supplierbreakstatus', models.IntegerField(blank=True, null=True)),
                ('employeebreakstatus', models.IntegerField(blank=True, null=True)),
                ('ataxcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ataxcode_dcdetailbreakdown_id', to='ataxcode.Ataxcode')),
                ('bankaccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount_dcdetailbreakdown_id', to='bankaccount.Bankaccount')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_dcdetailbreakdown_id', to='branch.Branch')),
                ('chartofaccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount_dcdetailbreakdown_id', to='chartofaccount.Chartofaccount')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_dcdetailbreakdown_id', to='customer.Customer')),
                ('dcdetail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetail_dcdetailbreakdown_id', to='debitcreditmemo.Dcdetail')),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'dcdetailbreakdown',
            },
        ),
        migrations.CreateModel(
            name='Dcdetailbreakdowntemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_counter', models.IntegerField()),
                ('secretkey', models.CharField(blank=True, max_length=255, null=True)),
                ('dcdetailtemp', models.CharField(blank=True, max_length=10, null=True)),
                ('datatype', models.CharField(blank=True, max_length=1, null=True)),
                ('dcmain', models.CharField(blank=True, max_length=10, null=True)),
                ('dcdetail', models.CharField(blank=True, max_length=10, null=True)),
                ('dcdetailbreakdown', models.CharField(blank=True, max_length=10, null=True)),
                ('dc_num', models.CharField(max_length=10)),
                ('dc_date', models.DateTimeField(blank=True, null=True)),
                ('chartofaccount', models.IntegerField(blank=True, null=True)),
                ('particular', models.TextField(blank=True, null=True)),
                ('bankaccount', models.IntegerField(blank=True, null=True)),
                ('department', models.IntegerField(blank=True, null=True)),
                ('employee', models.IntegerField(blank=True, null=True)),
                ('supplier', models.IntegerField(blank=True, null=True)),
                ('customer', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('branch', models.IntegerField(blank=True, null=True)),
                ('product', models.IntegerField(blank=True, null=True)),
                ('inputvat', models.IntegerField(blank=True, null=True)),
                ('outputvat', models.IntegerField(blank=True, null=True)),
                ('vat', models.IntegerField(blank=True, null=True)),
                ('wtax', models.IntegerField(blank=True, null=True)),
                ('ataxcode', models.IntegerField(blank=True, null=True)),
                ('debitamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('creditamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('balancecode', models.CharField(blank=True, max_length=1, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('customerbreakstatus', models.IntegerField(blank=True, null=True)),
                ('supplierbreakstatus', models.IntegerField(blank=True, null=True)),
                ('employeebreakstatus', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 458000))),
                ('postdate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 458000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdowntemp_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdowntemp_modify', to=settings.AUTH_USER_MODEL)),
                ('postby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdowntemp_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'dcdetailbreakdowntemp',
            },
        ),
        migrations.CreateModel(
            name='Dcdetailtemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_counter', models.IntegerField()),
                ('secretkey', models.CharField(blank=True, max_length=255, null=True)),
                ('dcmain', models.CharField(blank=True, max_length=10, null=True)),
                ('dcdetail', models.CharField(blank=True, max_length=10, null=True)),
                ('dc_num', models.CharField(max_length=10)),
                ('dc_date', models.DateTimeField(blank=True, null=True)),
                ('chartofaccount', models.IntegerField(blank=True, null=True)),
                ('bankaccount', models.IntegerField(blank=True, null=True)),
                ('department', models.IntegerField(blank=True, null=True)),
                ('employee', models.IntegerField(blank=True, null=True)),
                ('supplier', models.IntegerField(blank=True, null=True)),
                ('customer', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('branch', models.IntegerField(blank=True, null=True)),
                ('product', models.IntegerField(blank=True, null=True)),
                ('inputvat', models.IntegerField(blank=True, null=True)),
                ('outputvat', models.IntegerField(blank=True, null=True)),
                ('vat', models.IntegerField(blank=True, null=True)),
                ('wtax', models.IntegerField(blank=True, null=True)),
                ('ataxcode', models.IntegerField(blank=True, null=True)),
                ('debitamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('creditamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('balancecode', models.CharField(blank=True, max_length=1, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('customerbreakstatus', models.IntegerField(blank=True, null=True)),
                ('supplierbreakstatus', models.IntegerField(blank=True, null=True)),
                ('employeebreakstatus', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 456000))),
                ('postdate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 456000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailtemp_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailtemp_modify', to=settings.AUTH_USER_MODEL)),
                ('postby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailtemp_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'dcdetailtemp',
            },
        ),
        migrations.CreateModel(
            name='Dcmain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcnum', models.CharField(max_length=10, unique=True)),
                ('dcdate', models.DateField()),
                ('dcstatus', models.CharField(choices=[('F', 'For Approval'), ('A', 'Approved'), ('D', 'Disapproved')], default='F', max_length=1)),
                ('dctype', models.CharField(choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1)),
                ('customer_code', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_name', models.CharField(max_length=250)),
                ('outputvattype', models.CharField(choices=[('OUTV G', 'Output VAT - Goods'), ('OUTV S', 'Output VAT - Services')], max_length=6)),
                ('vatrate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('particulars', models.TextField()),
                ('approverresponse', models.CharField(blank=True, choices=[('A', 'Approved'), ('D', 'Disapproved')], max_length=1, null=True)),
                ('responsedate', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 17, 31, 0, 445000))),
                ('postdate', models.DateTimeField(blank=True, null=True)),
                ('isdeleted', models.IntegerField(default=0)),
                ('print_ctr', models.IntegerField(default=0)),
                ('actualapprover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_actual_approver', to=settings.AUTH_USER_MODEL)),
                ('branch', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_branch_id', to='branch.Branch')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_customer_id', to='customer.Customer')),
                ('dcartype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_artype_id', to='artype.Artype')),
                ('dcsubtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_subtype_id', to='debitcreditmemosubtype.Debitcreditmemosubtype')),
                ('designatedapprover', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_designated_approver', to=settings.AUTH_USER_MODEL)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_modify', to=settings.AUTH_USER_MODEL)),
                ('postby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_post', to=settings.AUTH_USER_MODEL)),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_vat_id', to='vat.Vat', validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'dcmain',
                'permissions': (('view_debitcreditmemo', 'Can view debit credit memo'), ('approve_assigneddc', 'Can approve assigned dc'), ('approve_alldc', 'Can approve all dc')),
            },
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='dcmain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_dcdetailbreakdown_id', to='debitcreditmemo.Dcmain'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_dcdetailbreakdown_id', to='department.Department'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_dcdetailbreakdown_id', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='enterby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdown_enter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='inputvat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inputvat_dcdetailbreakdown_id', to='inputvat.Inputvat'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='modifyby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdown_modify', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='outputvat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outputvat_dcdetailbreakdown_id', to='outputvat.Outputvat'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetailbreakdown_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_dcdetailbreakdown_id', to='product.Product'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_dcdetailbreakdown_id', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_dcdetailbreakdown_id', to='unit.Unit'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='vat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vat_dcdetailbreakdown_id', to='vat.Vat'),
        ),
        migrations.AddField(
            model_name='dcdetailbreakdown',
            name='wtax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wtax_dcdetailbreakdown_id', to='wtax.Wtax'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='dcmain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcmain_dcdetail_id', to='debitcreditmemo.Dcmain'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_dcdetail_id', to='department.Department'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_dcdetail_id', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='enterby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetail_enter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='inputvat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inputvat_dcdetail_id', to='inputvat.Inputvat'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='modifyby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetail_modify', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='outputvat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outputvat_dcdetail_id', to='outputvat.Outputvat'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='postby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dcdetail_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_dcdetail_id', to='product.Product'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_dcdetail_id', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_dcdetail_id', to='unit.Unit'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='vat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vat_dcdetail_id', to='vat.Vat'),
        ),
        migrations.AddField(
            model_name='dcdetail',
            name='wtax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wtax_dcdetail_id', to='wtax.Wtax'),
        ),
    ]
